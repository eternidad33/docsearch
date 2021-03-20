class School:
    # 名称, 曾用名, 地域, 官网
    name = ''
    name_used = ''
    region = ''
    official_website = ''

    def __init__(self, name='', name_used='', region='', official_website=''):
        self.name = name
        self.name_used = name_used
        self.region = region
        self.official_website = official_website


