from elasticsearch_dsl import Text, Date, DocType


class BlogPostIndex(DocType):
    author = Text()
    title = Text()
    text = Text()
    created_at = Date()
    updated_at = Date()

    class Meta:
        index = 'blogpost-index'

