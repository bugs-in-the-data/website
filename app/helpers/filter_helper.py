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
                'state': 'NONE',
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

    def getFilterObject(self):
        return self.filters

    def getLowestLevels(self):
        lowest = {}

        if self.filters['taxa']['order_name'] == 'NONE':
            lowest['taxa'] = 'Insecta'
        elif self.filters['taxa']['family'] == 'NONE':
            lowest['taxa'] = self.filters['taxa']['order_name']
        elif self.filters['taxa']['genus'] == 'NONE':
            lowest['taxa'] = self.filters['taxa']['family']
        elif self.filters['taxa']['species'] == 'NONE':
            lowest['taxa'] = self.filters['taxa']['genus']
        else:
            lowest['taxa'] = self.filters['taxa']['species']

        if self.filters['location']['state'] == 'NONE':
            lowest['location'] = 'All Locations'
        elif self.filters['location']['drainage'] == 'NONE':
            lowest['location'] = self.filters['location']['state']
        elif self.filters['location']['name'] == 'NONE':
            lowest['location'] = self.filters['location']['drainage']
        elif self.filters['location']['sample_name'] == 'NONE':
            lowest['location'] = self.filters['location']['name']
        else:
            lowest['location'] = self.filters['location']['sample_name']

        return lowest