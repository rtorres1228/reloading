

def result_dict(rs):
    return list(map(get_dict, rs))


def get_dict(rs):
    ret_dict = {}
  
    for obj in rs:
            ret_dict.update(clean_dict(obj.__dict__))
    return ret_dict

def clean_dict(m_dict):
    del m_dict['_sa_instance_state']
    return m_dict