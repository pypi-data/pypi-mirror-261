from . import _urls
from ._utils import auth_user_required
from ._request import ApiRequester
from ._auth import AuthClient
from .types import (
    LinkType,
    LinkVoteDownReason,
    LinkCommentSortType,
    LinkCommentVoteType,
    RequestType,
    EntriesSortType,
    EntriesLastUpdateType
)


class _WykopApiClientBase:
    def __init__(self, auth: AuthClient):
        self.auth = auth
        self.auth.check_authentication()

    def raw_request(self, url: str, type: RequestType, data: dict | None = None):
        """
        Umozliwia bezposrednie odpytanie Wykop API
        """
        match type:
            case RequestType.GET:
                return ApiRequester(url=url, token=self.auth.get_jwt_token()).get(params=data)
            case RequestType.POST:
                return ApiRequester(url=url, token=self.auth.get_jwt_token()).post(data=data)
            case RequestType.PUT:
                return ApiRequester(url=url, token=self.auth.get_jwt_token()).put(data=data)
            case RequestType.DELETE:
                return ApiRequester(url=url, token=self.auth.get_jwt_token()).delete()


class _WykopApiClientLinksMixin(_WykopApiClientBase):
    def links_list(
            self,
            type: LinkType,
            page: str | None = None,
            limit: int | None = None,
        ) -> dict:
        """
        Zwraca listę znalezisk
        UWAGA: Parametr page przyjmuje dla użytkowników niezalogowanych int z numerem strony, a dla zalogowanych hash strony.
        UWAGA2: Standardowa paginacja jest dostępna tylko dla użytkowników niezalogowanych. Paginacja dla użytkowników zalogowanych będzie zwracać hash next dla następnej strony i prev dla poprzedniej.
        UWAGA3: Dla parametru type=upcoming (wykopalisko) paginacja przyjmuje parametr page jako int z nr strony, zarówno dla użytkowników zalogowanych i niezalogowanych
        """
        return ApiRequester(
            url=_urls.LINKS_URL,
            token=self.auth.get_jwt_token()
        ).get(params={
            "type": type.value,
            "page": page,
            "limit": limit
        })

    @auth_user_required
    def links_vote_up_link(
            self,
            link_id: str
        ):
        """
        Wymagana zalogowania uzytkownika

        Wykopanie znaleziska
        """
        return ApiRequester(
            url=_urls.LINKS_VOTE_UP_URL(link_id),
            token=self.auth.get_jwt_token()
        ).post()
    
    @auth_user_required
    def links_vote_down_link(
            self,
            link_id: str,
            reason: LinkVoteDownReason
        ):
        """
        Wymaga zalogowania uzytkownika

        Zakopanie znaleziska
        """
        return ApiRequester(
            url=_urls.LINKS_VOTE_DOWN_URL(link_id, reason.value),
            token=self.auth.get_jwt_token()
        ).post()
    
    @auth_user_required
    def links_vote_revoke_link(
            self,
            link_id: str
        ):
        """
        Wymaga zalogowania uzytkownika

        Cofnięcie wykopania lub zakopania znaleziska
        """
        return ApiRequester(
            url=_urls.LINKS_VOTES_URL(link_id),
            token=self.auth.get_jwt_token()
        ).delete()


class _WykopApiClientLinkCommentsMixin(_WykopApiClientBase):
    def link_comments_list(
        self,
        link_id: str,
        sort: LinkCommentSortType = LinkCommentSortType.NEWEST,
        page: str | None = None,
        limit: int | None = None,
    ) -> dict:
        """
        Komentarze do znaleziska
        """
        return ApiRequester(
            url=_urls.LINK_COMMENTS_URL(link_id),
            token=self.auth.get_jwt_token()
        ).get(params={
            "sort": sort.value,
            "page": page,
            "limit": limit
        })
    
    @auth_user_required
    def link_comments_create_comment(
            self,
            link_id: str,
            content: str | None = None,
            photo: str | None = None,
            embed: str | None = None,
            adult: bool | None = None,

        ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Dodawanie nowego komentarza do wykopaliska
        """
        return ApiRequester(
            url=_urls.LINK_COMMENTS_URL(link_id),
            token=self.auth.get_jwt_token()
        ).post(data={
            "content": content,
            "photo": photo,
            "embed": embed,
            "adult": adult
        })
    
    @auth_user_required
    def link_comments_create_comment_to_comment(
            self,
            link_id: str,
            comment_id: str,
            content: str | None = None,
            photo: str | None = None,
            embed: str | None = None,
            adult: bool | None = None,

        ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Dodawanie nowego podkomentarza do istniejącego komentarza
        """
        return ApiRequester(
            url=_urls.LINK_COMMENTS_COMMENT_URL(link_id, comment_id),
            token=self.auth.get_jwt_token()
        ).post(data={
            "content": content,
            "photo": photo,
            "embed": embed,
            "adult": adult
        })
    
    @auth_user_required
    def link_comments_update_comment(
            self,
            link_id: str,
            comment_id: str,
            content: str | None = None,
            photo: str | None = None,
            embed: str | None = None,
            adult: bool | None = None,

        ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Edycja komentarza do wykopaliska
        """
        return ApiRequester(
            url=_urls.LINK_COMMENTS_COMMENT_URL(link_id, comment_id),
            token=self.auth.get_jwt_token()
        ).put(data={
            "content": content,
            "photo": photo,
            "embed": embed,
            "adult": adult
        })
    
    @auth_user_required
    def link_comments_delete_comment(
            self,
            link_id: str,
            comment_id: str
        ):
        """
        Wymaga zalogowania uzytkownika.

        Usuwanie komentarza do wykopaliska
        """
        return ApiRequester(
            url=_urls.LINK_COMMENTS_COMMENT_URL(link_id, comment_id),
            token=self.auth.get_jwt_token()
        ).delete()
    
    @auth_user_required
    def link_comments_vote_comment(
            self,
            link_id: str,
            comment_id: str,
            type: LinkCommentVoteType,
        ):
        """
        Wymaga zalogowania uzytkownika.

        Glosowanie na komentarz do wykopaliska
        """
        return ApiRequester(
            url=_urls.LINK_COMMENTS_COMMENT_VOTE_URL(link_id, comment_id, type.value),
            token=self.auth.get_jwt_token()
        ).post()
   
    @auth_user_required
    def link_comments_vote_revoke_comment(
            self,
            link_id: str,
            comment_id: str,
        ):
        """
        Wymaga zalogowania uzytkownika.

        Cofanie oceny komentarza do wykopaliska
        """
        return ApiRequester(
            url=_urls.LINK_COMMENTS_COMMENT_VOTE_REVOKE_URL(link_id, comment_id),
            token=self.auth.get_jwt_token()
        ).delete()


class _WykopApiClientTagsMixin(_WykopApiClientBase):
    def tags_get_popular(self) -> dict:
        """
        Zwraca listę popularnych tagów.
        """
        return ApiRequester(
            url=_urls.TAGS_POPULAR_URL,
            token=self.auth.get_jwt_token()
        ).get()
    
    def tags_get_popular_user_tags(self) -> dict:
        """
        Kolekcja popularnych tagów autorskich (max do 10 wyników)
        """
        return ApiRequester(
            url=_urls.TAGS_POPULAR_USER_URL,
            token=self.auth.get_jwt_token()
        ).get()
        
    def tags_get_related_tag(self, tag: str) -> dict:
        """
        Kolekcja powiązanych tagów (max do 10 wyników)
        """
        return ApiRequester(
            url=_urls.TAGS_RELATED_TAG_URL(tag),
            token=self.auth.get_jwt_token()
        ).get()
    
    def tags_get_detail_of_tag(self, tag: str) -> dict:
        """
        Szczegóły tagu
        """
        return ApiRequester(
            url=_urls.TAGS_DETAIL_TAG_URL(tag),
            token=self.auth.get_jwt_token()
        ).get()
    
    @auth_user_required
    def tags_edit_tag(self, tag: str, photo: str, description: str) -> str:
        """
        Wymaga zalogowania uzytkownika.

        Właściciel tagu może modyfikować tło (base64 str) oraz opis tagu.
        """
        return ApiRequester(
            url=_urls.TAGS_DETAIL_TAG_URL(tag),
            token=self.auth.get_jwt_token()
        ).put({
            "photo": photo,
            "description": description
        })
    
    def tags_get_stream_of_tag(
            self,
            tag: str,
            page: str | None = None,
            limit: int | None = None,
            year: int | None = None,
            month: int | None = None
        ) -> dict:
        """
        Zwraca pełną liste wpisów i znalezisk z konkretnego tagu UWAGA: 
        Parametr page przyjmuje dla użytkowników niezalogowanych int z numerem strony, a dla zalogowanych hash strony. 
        UWAGA2: Standardowa paginacja jest dostępna tylko dla użytkowników niezalogowanych. 
        Paginacja dla użytkowników zalogowanych będzie zwracać hash next dla następnej strony i prev dla poprzedniej.
        """
        return ApiRequester(
            url=_urls.TAGS_STREAM_TAG_URL(tag),
            token=self.auth.get_jwt_token()
        ).get(params={
            "page": page,
            "limit": limit,
            "year": year,
            "month": month
        })
    
    def tags_get_tag_owners(
            self,
            tag: str,
        ) -> dict:
        """
        Kolekcja autorów tagu (short profile)
        """
        return ApiRequester(
            url=_urls.TAGS_TAG_OWNERS_URL(tag),
            token=self.auth.get_jwt_token()
        ).get()


class _WykopApiClientArticleMixin(_WykopApiClientBase):
    def articles_list_by_tag(
            self,
            tag: str,
            page: str | None = None,
            limit: int | None = None,
            year: int | None = None,
            month: int | None = None
        ) -> dict:
        """
        Zwraca pełną liste artykułów konkretnego tagu 
        UWAGA: Parametr page przyjmuje dla użytkowników niezalogowanych int z numerem strony, a dla zalogowanych hash strony. 
        UWAGA2: Standardowa paginacja jest dostępna tylko dla użytkowników niezalogowanych. 
        Paginacja dla użytkowników zalogowanych będzie zwracać hash next dla następnej strony i prev dla poprzedniej.
        """
        return ApiRequester(
            url=_urls.TAGS_STREAM_TAG_URL(tag),
            token=self.auth.get_jwt_token()
        ).get(params={
            "type": "article",
            "page": page,
            "limit": limit,
            "year": year,
            "month": month
        })
    
    def articles_get_article(
        self,
        article_id: str
    ) -> dict:
        """
        Pobranie informacji o artykule
        """
        return ApiRequester(
            url=_urls.ARTICLES_ARTICLE_URL(article_id),
            token=self.auth.get_jwt_token()
        ).get()


class _WykopApiClientEntriesMixin(_WykopApiClientBase):
    @auth_user_required
    def entries_create(
            self,
            content: str | None = None,
            photo: str | None = None,
            embed: str | None = None,
            adult: bool | None = None,

        ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Dodawanie nowego wpisu na mikroblogu
        """
        return ApiRequester(
            url=_urls.ENTRIES_URL,
            token=self.auth.get_jwt_token()
        ).post(data={
            "content": content,
            "photo": photo,
            "embed": embed,
            "adult": adult
        })
    
    def entries_list(
        self,
        sort: EntriesSortType = EntriesSortType.HOT,
        last_update: EntriesLastUpdateType = EntriesLastUpdateType.TWELVE,
        page: str | None = None,
        limit: int | None = None,
    ) -> dict:
        """
        Zwraca wpisy z mikrobloga. 
        UWAGA: Parametr page przyjmuje dla użytkowników niezalogowanych int z numerem strony, a dla zalogowanych hash strony. 
        UWAGA2: Standardowa paginacja jest dostępna tylko dla użytkowników niezalogowanych. 
        Paginacja dla użytkowników zalogowanych będzie zwracać hash next dla następnej strony i prev dla poprzedniej.
        """
        return ApiRequester(
            url=_urls.ENTRIES_URL,
            token=self.auth.get_jwt_token()
        ).get(params={
            "sort": sort.value,
            "last_update": last_update.value,
            "page": page,
            "limit": limit
        })
    
    def entries_list_by_tag(
            self,
            tag: str,
            page: str | None = None,
            limit: int | None = None,
            year: int | None = None,
            month: int | None = None
        ) -> dict:
        """
        Zwraca pełną liste wpisów konkretnego tagu 
        UWAGA: Parametr page przyjmuje dla użytkowników niezalogowanych int z numerem strony, a dla zalogowanych hash strony. 
        UWAGA2: Standardowa paginacja jest dostępna tylko dla użytkowników niezalogowanych. 
        Paginacja dla użytkowników zalogowanych będzie zwracać hash next dla następnej strony i prev dla poprzedniej.
        """
        return ApiRequester(
            url=_urls.TAGS_STREAM_TAG_URL(tag),
            token=self.auth.get_jwt_token()
        ).get(params={
            "type": "entry",
            "page": page,
            "limit": limit,
            "year": year,
            "month": month
        })
    
    def entries_get_entry(
        self,
        entry_id: str
    ) -> dict:
        """
        Pobranie wpisu z mikrobloga
        """
        return ApiRequester(
            url=_urls.ENTRIES_ENTRY_URL(entry_id),
            token=self.auth.get_jwt_token()
        ).get()
    
    @auth_user_required
    def entries_update_entry(
        self,
        entry_id: str,
        content: str | None = None,
        photo: str | None = None,
        embed: str | None = None,
        adult: bool | None = None,
    ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Edycja wpisu z mikrobloga
        """
        return ApiRequester(
            url=_urls.ENTRIES_ENTRY_URL(entry_id),
            token=self.auth.get_jwt_token()
        ).put({
            "content": content,
            "photo": photo,
            "embed": embed,
            "adult": adult
        })
    
    @auth_user_required
    def entries_delete_entry(
        self,
        entry_id: str
    ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Usuwanie wpisu z mikrobloga
        """
        return ApiRequester(
            url=_urls.ENTRIES_ENTRY_URL(entry_id),
            token=self.auth.get_jwt_token()
        ).delete()
    
    @auth_user_required
    def entries_vote_up_entry(
        self,
        entry_id: str
    ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Głosowanie na wpis z mikrobloga
        """
        return ApiRequester(
            url=_urls.ENTRIES_ENTRY_VOTES_URL(entry_id),
            token=self.auth.get_jwt_token()
        ).post()
    
    @auth_user_required
    def entries_vote_revoke_entry(
        self,
        entry_id: str
    ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Cofnięcie głosu na wpis z mikrobloga
        """
        return ApiRequester(
            url=_urls.ENTRIES_ENTRY_VOTES_URL(entry_id),
            token=self.auth.get_jwt_token()
        ).delete()


class _WykopApiClientEntryCommentsMixin(_WykopApiClientBase):
    def entry_comments_list(
        self,
        entry_id: str,
        page: str | None = None,
        limit: int | None = None,
    ) -> dict:
        """
        Komentarze do wpisu z mikrobloga
        """
        return ApiRequester(
            url=_urls.ENTRY_COMMENTS_URL(entry_id),
            token=self.auth.get_jwt_token()
        ).get(params={
            "page": page,
            "limit": limit
        })
    
    @auth_user_required
    def entry_comments_create_comment(
            self,
            entry_id: str,
            content: str | None = None,
            photo: str | None = None,
            embed: str | None = None,
            adult: bool | None = None,

        ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Dodawanie nowego komentarza do wpisu na mikroblogu
        """
        return ApiRequester(
            url=_urls.ENTRY_COMMENTS_URL(entry_id),
            token=self.auth.get_jwt_token()
        ).post(data={
            "content": content,
            "photo": photo,
            "embed": embed,
            "adult": adult
        })

    @auth_user_required
    def entry_comments_update_comment(
            self,
            entry_id: str,
            comment_id: str,
            content: str | None = None,
            photo: str | None = None,
            embed: str | None = None,
            adult: bool | None = None,

        ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Edycja komentarza do wpisu na mikroblogu
        """
        return ApiRequester(
            url=_urls.ENTRY_COMMENTS_COMMENT_URL(entry_id, comment_id),
            token=self.auth.get_jwt_token()
        ).put(data={
            "content": content,
            "photo": photo,
            "embed": embed,
            "adult": adult
        })
    
    @auth_user_required
    def entry_comments_delete_comment(
        self,
        entry_id: str,
        comment_id: str
    ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Usuwanie komentarza do wpisu z mikrobloga
        """
        return ApiRequester(
            url=_urls.ENTRY_COMMENTS_COMMENT_URL(entry_id, comment_id),
            token=self.auth.get_jwt_token()
        ).delete()
    
    @auth_user_required
    def entry_comments_vote_up_comment(
        self,
        entry_id: str,
        comment_id: str
    ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Głosowanie na komentarz do wpisu z mikrobloga
        """
        return ApiRequester(
            url=_urls.ENTRY_COMMENTS_VOTES_URL(entry_id, comment_id),
            token=self.auth.get_jwt_token()
        ).post()
    
    @auth_user_required
    def entry_comments_vote_revoke_comment(
        self,
        entry_id: str,
        comment_id: str
    ) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Cofanie głosu na komentarz do wpisu z mikrobloga
        """
        return ApiRequester(
            url=_urls.ENTRY_COMMENTS_VOTES_URL(entry_id, comment_id),
            token=self.auth.get_jwt_token()
        ).delete()


class _WykopApiClientNotificationsMixin(_WykopApiClientBase):
    @auth_user_required
    def notifinations_entries_list(self) -> dict:
        """
        Wymaga zalogowania uzytkownika.

        Pobranie notyfikacji
        """
        return ApiRequester(
            url=_urls.NOTIFICATIONS_ENTRIES_URL,
            token=self.auth.get_jwt_token()
        ).get()


class WykopApiClient(
    _WykopApiClientLinksMixin,
    _WykopApiClientLinkCommentsMixin,
    _WykopApiClientArticleMixin,
    _WykopApiClientTagsMixin,
    _WykopApiClientEntriesMixin,
    _WykopApiClientEntryCommentsMixin,
    _WykopApiClientNotificationsMixin
):
    pass
