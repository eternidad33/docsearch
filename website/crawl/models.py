# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

from .utils import extractAuthorName, extractArticleFileName, extractOrganizationName, extractBaseID


class Article(models.Model):
    url = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'article'


class Author(models.Model):
    url = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    major = models.CharField(max_length=255, blank=True, null=True)
    sum_publish = models.IntegerField(blank=True, null=True)
    sum_download = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'author'


class Organization(models.Model):
    url = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    used_name = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'organization'


class ReArticleAuthor(models.Model):
    url_article = models.CharField(primary_key=True, max_length=255)
    url_author = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        article = extractArticleFileName(self.url_article)
        name = extractAuthorName(self.url_author)
        return article + '--' + name

    def getArticle(self):
        return extractArticleFileName(self.url_article)

    def getAuthor(self):
        return extractAuthorName(self.url_author)

    getArticle.short_description = '文章'
    getAuthor.short_description = '作者'

    class Meta:
        managed = False
        db_table = 're_article_author'
        unique_together = (('url_article', 'url_author'),)


class ReArticleSource(models.Model):
    url_article = models.CharField(primary_key=True, max_length=255)
    url_source = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        article = extractArticleFileName(self.url_article)
        source = extractBaseID(self.url_source)
        return article + '--' + source

    def getArticle(self):
        return extractArticleFileName(self.url_article)

    def getSource(self):
        return extractBaseID(self.url_source)

    getArticle.short_description = '文章'
    getSource.short_description = '来源'

    class Meta:
        managed = False
        db_table = 're_article_source'
        unique_together = (('url_article', 'url_source'),)


class ReAuthorOrganization(models.Model):
    url_author = models.CharField(primary_key=True, max_length=255)
    url_organization = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        author = extractAuthorName(self.url_author)
        organization = extractOrganizationName(self.url_organization)
        return author + '---' + organization

    def getAuthor(self):
        return extractAuthorName(self.url_author)

    def getOrganization(self):
        return extractOrganizationName(self.url_organization)

    getAuthor.short_description = '作者'
    getOrganization.short_description = '组织'

    class Meta:
        managed = False
        db_table = 're_author_organization'


class ReTeacherStudent(models.Model):
    url_teacher = models.CharField(primary_key=True, max_length=255)
    url_student = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        teacher = extractAuthorName(self.url_teacher)
        student = extractAuthorName(self.url_student)
        return teacher + '---' + student

    def getTeacher(self):
        return extractAuthorName(self.url_teacher)

    def getStudent(self):
        return extractAuthorName(self.url_student)

    getTeacher.short_description = '老师'
    getStudent.short_description = '学生'

    class Meta:
        managed = False
        db_table = 're_teacher_student'
        unique_together = (('url_teacher', 'url_student'),)


class Source(models.Model):
    url = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    basic_info = models.CharField(max_length=255, blank=True, null=True)
    publish_info = models.CharField(max_length=255, blank=True, null=True)
    evaluation = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'source'
