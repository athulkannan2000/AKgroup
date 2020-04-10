from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = '**uname**'  # <- enter username here
insta_password = '**pass**'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)
    #session.set_dont_include(["friend1", "friend2", "friend3"])
    #session.set_dont_like(["pizza", "#store"])
    session.set_smart_hashtags(['technology', 'innovation'], limit=3, sort='top', log_tags=True)
    session.like_by_tags(amount=10, use_smart_hashtags=True)
