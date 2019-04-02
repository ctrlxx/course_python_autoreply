# coding=utf8
# 使用前需关注小冰公众号

from itchat_lib import *

if __name__ == '__main__':
    WAKEN_MSG = [u"小冰", u"小冰小冰", u"小冰呢", u"小冰呢？", u"小冰回来", u"小冰出来", u"在？", u"在吗", u'苏雷']
    HIBERNATE_MSG = [u"小冰住嘴", u"小冰闭嘴", u"滚", u"你滚", u"你闭嘴", u"下去吧", u"小冰下去", u"小冰退下"]
    TRIGGER_MSG = WAKEN_MSG + HIBERNATE_MSG

    itchat.auto_login()

    my_user_name = itchat.get_friends(update=True)[0]["UserName"]
    xiao_bing_user_name = itchat.search_mps(name=u'小冰')[0]["UserName"]  # mps公众号/服务号

    peer_list = set()
    asker_queue = deque()
    unprocessed_questions = {}
    current_asker_id_name = None
    last_xiaobing_response_ts = None
    debug = True
    is_xiaobing_busy = False

    process_message()
    itchat.run()
