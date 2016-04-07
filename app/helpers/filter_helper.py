import datetime

class FilterHelperModel():
    def __init__(self):
        self.filters = {
            'taxa': {
                'order_name': 'NONE',
                'family': 'NONE',
                'genus': 'NONE',
                'species': 'NONE',
            },
            'location': {
                'installation': 'NONE',
                'drainage': 'NONE',
                'name': 'NONE',
                'sample_name': 'NONE',
            },
            'date': {
                'start': '01/01/2009',
                'end': '01/01/2014',
            },
            'season': [
                'Spring',
                'Summer',
                'Fall',
                'Winter',
            ],
        }

    def getFilterObject(self):
        return self.filters

    def getSubSampleSubLocation(self):
        return self.subSampleSubLocation

    def getStartDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def getSubTaxa(self):
        return self.subTaxa

    def handleFilterPostData(self, post):
        # take post data, format and create a filter object
        self.filters['date']['start'] = post.get('start')
        self.filters['date']['end'] = post.get('end')

        self.filters['season'] = post.getlist('ft_1[]')

        for level in post['ft_2[]'].split(';'):
            key, value = level.split('=')
            self.filters['taxa'][key] = value

        for level in post['ft_3[]'].split(';'):
            key, value = level.split('=')
            self.filters['location'][key] = value

        return self.filters

    def refineSubsampleQuery(self, query):
        if self.filters['taxa']['species'] != 'NONE':
            query = query.filter(species=self.filters['taxa']['species'])
        elif self.filters['taxa']['genus'] != 'NONE':
            query = query.filter(genus=self.filters['taxa']['genus'])
        elif self.filters['taxa']['family'] != 'NONE':
            query = query.filter(family=self.filters['taxa']['family'])
        elif self.filters['taxa']['order_name'] != 'NONE':
            query = query.filter(order_name=self.filters['taxa']['order_name'])
        else:
            pass

        if self.filters['location']['sample_name'] != 'NONE':
            query = query.filter(sample__sample_name=self.filters['location']['sample_name'])
        elif self.filters['location']['name'] != 'NONE':
            query = query.filter(sample__site__name=self.filters['location']['name'])
        elif self.filters['location']['drainage'] != 'NONE':
            query = query.filter(sample__site__drainage=self.filters['location']['drainage'])
        elif self.filters['location']['installation'] != 'NONE':
            query = query.filter(sample__site__installation=self.filters['location']['installation'])
        else:
            pass

        try:
            query = query.filter(sample__date__gte=datetime.datetime.strptime(self.startDate, '%m/%d/%Y').strftime('%Y-%m-%d'))
        except ValueError:
            print "incorrect start date"
        try:
            query = query.filter(sample__date__lte=datetime.datetime.strptime(self.endDate, '%m/%d/%Y').strftime('%Y-%m-%d'))
        except ValueError:
            print "incorrect end date"

        query = query.filter(sample__season__in=self.filters['season'])

        return query

    def refineSampleQuery(self, query):
        if self.filters['location']['sample_name'] != 'NONE':
            query = query.filter(sample_name=self.filters['location']['sample_name'])
        elif self.filters['location']['name'] != 'NONE':
            query = query.filter(site__name=self.filters['location']['name'])
        elif self.filters['location']['drainage'] != 'NONE':
            query = query.filter(site__drainage=self.filters['location']['drainage'])
        elif self.filters['location']['installation'] != 'NONE':
            query = query.filter(site__installation=self.filters['location']['installation'])
        else:
            pass

        try:
            query = query.filter(date__gte=datetime.datetime.strptime(self.startDate, '%m/%d/%Y').strftime('%Y-%m-%d'))
        except ValueError:
            print "incorrect start date"
        try:
            query = query.filter(date__lte=datetime.datetime.strptime(self.endDate, '%m/%d/%Y').strftime('%Y-%m-%d'))
        except ValueError:
            print "incorrect end date"

        query = query.filter(season__in=self.filters['season'])

        return query

    def getLowestLevels(self):
        lowest = {}

        self.startDate = self.filters['date']['start']
        self.endDate = self.filters['date']['end']

        if self.filters['taxa']['order_name'] == 'NONE':
            self.subTaxa = 'order_name'
            lowest['taxa'] = 'Insecta'
        elif self.filters['taxa']['family'] == 'NONE':
            self.subTaxa = 'family'
            lowest['taxa'] = self.filters['taxa']['order_name']
        elif self.filters['taxa']['genus'] == 'NONE':
            self.subTaxa = 'genus'
            lowest['taxa'] = self.filters['taxa']['family']
        elif self.filters['taxa']['species'] == 'NONE':
            self.subTaxa = 'species'
            lowest['taxa'] = self.filters['taxa']['genus']
        else:
            self.subTaxa = 'species'
            lowest['taxa'] = self.filters['taxa']['species']

        if self.filters['location']['installation'] == 'NONE':
            self.subSampleSubLocation = 'sample__site__installation'
            self.sampleSubLocation = 'site__installation'
            lowest['location'] = 'All Locations'
        elif self.filters['location']['drainage'] == 'NONE':
            self.sampleSubLocation = 'site__drainage'
            self.subSampleSubLocation = 'sample__site__drainage'
            lowest['location'] = self.filters['location']['installation']
        elif self.filters['location']['name'] == 'NONE':
            self.sampleSubLocation = 'site__name'
            self.subSampleSubLocation = 'sample__site__name'
            lowest['location'] = self.filters['location']['drainage']
        elif self.filters['location']['sample_name'] == 'NONE':
            self.sampleSubLocation = 'sample_name'
            self.subSampleSubLocation = 'sample__sample_name'
            lowest['location'] = self.filters['location']['name']
        else:
            self.sampleSubLocation = 'sample_name'
            self.subSampleSubLocation = 'sample__sample_name'
            lowest['location'] = self.filters['location']['sample_name']

        return lowest
