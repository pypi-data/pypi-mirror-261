from afeng_tools.fastapi_tool.common.po_service.article_po_service_ import ArticlePoService
from afeng_tools.fastapi_tool.common.po_service.blacklist_po_service_ import BlacklistPoService
from afeng_tools.fastapi_tool.common.po_service.category_po_service_ import CategoryPoService
from afeng_tools.fastapi_tool.common.po_service.group_po_service_ import GroupPoService
from afeng_tools.fastapi_tool.common.po_service.link_po_service_ import LinkPoService
from afeng_tools.fastapi_tool.common.po_service.resource_po_service_ import ResourcePoService
from afeng_tools.fastapi_tool.common.po_service.sitemap_po_service_ import SitemapPoService
from afeng_tools.fastapi_tool.common.po_service.tag_po_service_ import TagPoService


class CommonPoService:
    """通用po服务"""

    def __init__(self, db_code: str):
        self.db_code = db_code

    def article_po_service(self, ArticleInfoPo: type) -> ArticlePoService:
        return ArticlePoService(self.db_code, ArticleInfoPo)

    def blacklist_po_service(self, BlacklistInfoPo: type) -> BlacklistPoService:
        return BlacklistPoService(self.db_code, BlacklistInfoPo)

    def category_po_service(self, CategoryInfoPo: type) -> CategoryPoService:
        return CategoryPoService(self.db_code, CategoryInfoPo)

    def group_po_service(self, GroupInfoPo: type) -> GroupPoService:
        return GroupPoService(self.db_code, GroupInfoPo)

    def link_po_service(self, LinkInfoPo: type) -> LinkPoService:
        return LinkPoService(self.db_code, LinkInfoPo)

    def resource_po_service(self, ResourceInfoPo: type) -> ResourcePoService:
        return ResourcePoService(self.db_code, ResourceInfoPo)

    def sitemap_po_service(self, SitemapInfoPo: type) -> SitemapPoService:
        return SitemapPoService(self.db_code, SitemapInfoPo)

    def tag_po_service(self, TagInfoPo: type) -> TagPoService:
        return TagPoService(self.db_code, TagInfoPo)
