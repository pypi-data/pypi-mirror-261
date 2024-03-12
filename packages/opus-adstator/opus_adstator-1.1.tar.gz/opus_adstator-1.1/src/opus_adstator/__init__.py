import os
from datetime import datetime
import traceback
from git import cmd as git_cmd


def get_utc_timestamp(with_decimal: bool=False): 
    epoch = datetime(1970,1,1,0,0,0)
    now = datetime.utcnow()
    timestamp = (now - epoch).total_seconds()
    if with_decimal:
        return timestamp
    return int(timestamp)


def is_debug_set_in_environment()->bool:    # pragma: no cover
    try:
        env_debug = os.getenv('DEBUG', '0').lower()
        if env_debug in ('1','true','t','enabled', 'e'):
            return True
    except:
        pass
    return False


def is_url_a_git_repo(url: str)->bool:
    try:
        if '%00' in url:
            url = url[0:url.find('%00')]
        remote_refs = {}
        g = git_cmd.Git()
        for ref in g.ls_remote(url).split('\n'):
            hash_ref_list = ref.split('\t')
            remote_refs[hash_ref_list[1]] = hash_ref_list[0]
        if len(remote_refs) > 0:
            return True
    except:
        traceback.print_exc()
    return False
