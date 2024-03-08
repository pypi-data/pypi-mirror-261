from unittest import TestCase
import os

from src.wykop_sdk_reloaded.v3.client import AuthClient, WykopApiClient
from src.wykop_sdk_reloaded.v3.types import LinkType, LinkVoteDownReason, LinkCommentVoteType, RequestType, EntriesSortType, MediaPhotosType
from src.wykop_sdk_reloaded.exceptions import AuthError


env = os.getenv


class TestReadOnlyWykopApiV3Client(TestCase):
    def setUp(self):
        auth = AuthClient()
        auth.authenticate_app(env("WYKOP_APP_KEY"), env("WYKOP_APP_SECRET"))

        self.api = WykopApiClient(auth)    

    def test_read_only_operations(self):
        tag = "wykop"
        
        self.api.tags_get_detail_of_tag(tag)
        self.api.tags_get_popular()
        self.api.tags_get_popular_user_tags()
        self.api.tags_get_related_tag(tag)
        self.api.tags_get_stream_of_tag(tag)
        self.api.tags_get_tag_owners(tag)
        self.api.entries_list()

    def test_not_permitted(self):
        with self.assertRaises(AuthError):
            self.api.notifinations_entries_list()
            self.api.entries_create("lorem " * 40)

    
    def test_raw_request(self):
        self.assertGreater(
            len(self.api.raw_request("https://wykop.pl/api/v3/tags/popular", RequestType.GET)["data"]),
            0
        )


class TestWykopApiV3Client(TestCase):
    def setUp(self):
        auth = AuthClient()
        auth.authenticate_user(
            token=env("WYKOP_USER_TOKEN"),
            refresh_token=env("WYKOP_USER_REFRESH_TOKEN")
        )
        
        self.api = WykopApiClient(auth)

    def test_tags(self):
        tag = "wykop"

        self.api.tags_get_detail_of_tag(tag)
        self.api.tags_get_popular()
        self.api.tags_get_popular_user_tags()
        self.api.tags_get_related_tag(tag)
        self.api.tags_get_stream_of_tag(tag)
        self.api.tags_get_tag_owners(tag)

    def test_entries(self):
        response = self.api.entries_create("lorem " * 40)
        entry_id = str(response["data"]["id"])

        self.api.entries_get_entry(entry_id)
        self.api.entries_update_entry(entry_id, 'ipsum'* 20)

        self.api.entry_comments_list(entry_id)

        response = self.api.entry_comments_create_comment(entry_id, "ipsum lorem" * 5)
        entry_comment_id = str(response["data"]["id"])
        
        self.api.entry_comments_list(entry_id)
        self.api.entry_comments_update_comment(entry_id, entry_comment_id, "test " * 5)
        self.api.entry_comments_delete_comment(entry_id, entry_comment_id)

        self.api.entries_delete_entry(entry_id)

    def test_entries_voting(self):
        self.api.entries_list(sort=EntriesSortType.NEWEST)
        response = self.api.entries_list_by_tag("wykop")
        entry_id = response["data"][0]["id"]

        self.api.entries_vote_up_entry(entry_id)
        self.api.entries_vote_revoke_entry(entry_id)

    def test_links(self):
        response = self.api.links_list(LinkType.HOMEPAGE)
        link_id = response["data"][0]["id"]

        self.api.links_vote_down_link(link_id, LinkVoteDownReason.INAPPROPRIATE)
        self.api.links_vote_revoke_link(link_id)
        self.api.links_vote_up_link(link_id)
        self.api.links_vote_revoke_link(link_id)

        response = self.api.link_comments_list(link_id)
        comment_id = response["data"][0]["id"]
        self.api.link_comments_vote_comment(link_id, comment_id, LinkCommentVoteType.UP)
        self.api.link_comments_vote_revoke_comment(link_id, comment_id)

        response = self.api.link_comments_create_comment(link_id, "test "* 10)
        own_comment_id = response["data"]["id"]

        self.api.link_comments_update_comment(link_id, own_comment_id, content="albo" * 10)
        response = self.api.link_comments_create_comment_to_comment(link_id, own_comment_id, content="albo" * 10)
        own_comment_to_comment_id = response["data"]["id"]

        self.api.link_comments_delete_comment(link_id, own_comment_id)
        self.api.link_comments_delete_comment(link_id, own_comment_to_comment_id)
        
    def test_notifications(self):
        self.api.notifinations_entries_list()

    def test_media_photos(self):
        response = self.api.photos_upload_url(
            "https://i.ibb.co/Yb1C27t/Zrzut-ekranu-2024-03-7-o-12-45-54.png",
            MediaPhotosType.COMMENTS
        )
        key = response["data"]["key"]

        self.api.photos_delete_photo(key)

    def test_media_embed(self):
        response = self.api.embed_upload_url(
            "https://www.youtube.com/watch?v=rtL5oMyBHPs&list=RDMMFa1UPDtZBYY&index=7",
        )
        assert response["data"]["key"]

    def test_link_draft(self):
        self.api.links_draft_list()

        response = self.api.links_draft_create_step_one(
            url="https://youtu.be/dvgZkm1xWPE?si=4lRM8tevSl9tvClT"
        )
        key = response["data"]["key"]

        self.api.links_draft_get_draft(key)
        self.api.links_draft_remove_draft(key)
        
        
        response = self.api.links_draft_create_step_one(
            url="https://youtu.be/dvgZkm1xWPE?si=4lRM8tevSl9tvClT"
        )
        key = response["data"]["key"]
        self.api.links_draft_create_step_two(
            key=key,
            title="Coldplay Viva La Vida 4",
            description="lorem " * 10,
            tags=["muzyka"],
            adult=False
        )
        response = self.api.profiles_get_profile_links_added(env("WYKOP_USERNAME"))
        link_id = response["data"][0]["id"]
        self.api.links_remove_link(link_id)
