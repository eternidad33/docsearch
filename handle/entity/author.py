# 姓名,学校,专业,总发布量,总下载量,专注领域,作者文献,导师,学生

class Author:

    def __init__(self, url='', name='', school='', major='', sum_publish='', sum_download='', fields=[], articles=[],
                 teacher='', students=[]):
        self.url = url
        self.name = name
        self.school = school
        self.major = major
        self.sum_publish = sum_publish
        self.sum_download = sum_download
        self.fields = fields
        self.articles = articles
        self.teacher = teacher
        self.students = students
