# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.exporters import *
import logging
logger=logging.getLogger(__name__)
class BaseExportPipeLine(object):
    def __init__(self,**kwargs):
        self.files = {}
        self.exporter=kwargs.pop("exporter",None)
        self.dst=kwargs.pop("dst",None)
        self.option=kwargs
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open(self.dst, 'wb')
        self.files[spider] = file
        self.exporter = self.exporter(file,**self.option)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

# 
# 'fields_to_export':["url","edit_url","title"] 设定只导出部分字段,以下几个pipeline都支持这个参数
# 'export_empty_fields':False 设定是否导出空字段 以下几个pipeline都支持这个参数
# 'encoding':'utf-8' 设定默认编码，以下几个pipeline都支持这个参数
# 'indent' :1： 设置缩进，这个参数主要给JsonLinesExportPipeline使用
# "item_element":"item"设置xml节点元素的名字，只能XmlExportPipeline使用,效果是<item></item>
# "root_element":"items"设置xml根元素的名字，只能XmlExportPipeline使用，效果是<items>里面是很多item</items>
# "include_headers_line":True 是否包含字段行， 只能CsvExportPipeline使用
# "join_multivalued":","设置csv文件的分隔符号， 只能CsvExportPipeline使用
# 'protocol':2设置PickleExportPipeline 导出协议，只能PickleExportPipeline使用
# "dst":"items.json" 设置目标位置
class JsonExportPipeline(BaseExportPipeLine):
    def __init__(self):
        option={"exporter":JsonItemExporter,"dst":"items.json","encoding":"utf-8","indent":4,}
        super(JsonExportPipeline, self).__init__(**option)
class JsonLinesExportPipeline(BaseExportPipeLine):
    def __init__(self):
        option={"exporter":JsonLinesItemExporter,"dst":"items.jl","encoding":"utf-8"}
        super(JsonLinesExportPipeline, self).__init__(**option)
class XmlExportPipeline(BaseExportPipeLine):
    def __init__(self):
        option={"exporter":XmlItemExporter,"dst":"items.xml","item_element":"item","root_element":"items","encoding":'utf-8'}
        super(XmlExportPipeline, self).__init__(**option)
class CsvExportPipeline(BaseExportPipeLine):
    def __init__(self):
        # 设置分隔符的这个，我这里测试是不成功的
        option={"exporter":CsvItemExporter,"dst":"items.csv","encoding":"utf-8","include_headers_line":True, "join_multivalued":","}
        super(CsvExportPipeline, self).__init__(**option)
class  PickleExportPipeline(BaseExportPipeLine):
    def __init__(self):
        option={"exporter":PickleItemExporter,"dst":"items.pickle",'protocol':2}
        super(PickleExportPipeline, self).__init__(**option)
class  MarshalExportPipeline(BaseExportPipeLine):
    def __init__(self):
        option={"exporter":MarshalItemExporter,"dst":"items.marsha"}
        super(MarshalExportPipeline, self).__init__(**option)
class  PprintExportPipeline(BaseExportPipeLine):
    def __init__(self):
        option={"exporter":PprintItemExporter,"dst":"items.pprint.jl"}
        super(PprintExportPipeline, self).__init__(**option)
