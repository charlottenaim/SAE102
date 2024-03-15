def test_create_network():
    assert create_network(amis) == {'Alice': ['Bob', 'Dominique'],
                                    'Bob': ['Alice', 'Charlie', 'Dominique'],
                                    'Charlie': ['Bob'],
                                    'Dominique': ['Alice', 'Bob']}
    assert not create_network(list_of_friends) == ['Léo','Thierry','Léo','Valentin','Léo','Axel']
    assert create_network(list_of_friends) != ['Thomas','Daria','Thomas','Carole','Thierry','Axel','Valentin','Andrea']
    print("La fonction create_network est ok")

test_create_network()
    
def test_get_people(network):
    assert get_people() == 
    assert not get_people() == 
    assert get_people() != 
    print("La fonction get_people() est ok")

test_get_people()
    
def test_are_friends(network, person1, person2):
    assert are_friends() == 
    assert not are_friends() == 
    assert are_friends() != 
    print("La fonction are_friends() est ok")
    
test_are_friends()

def test_all_his_friends(network, person, group):
    assert all_his_friends() == 
    assert not all_his_friends() == 
    assert all_his_friends() != 
    print("La fonction all_his_friends() est ok")
    
test_all_his_friends()

def test_is_a_community(network, group):
    assert is_a_community() == 
    assert not is_a_community() == 
    assert is_a_community() != 
    print("La fonction is_a_community() est ok")
    
test_is_a_community()

def test_find_community(network, group):
    assert find_community() == 
    assert not find_community() == 
    assert find_community() != 
    print("La fonction find_community() est ok")
    
test_find_community()

def test_pre_order_by_decreasing_popularity(network,group,k):
    assert pre_order_by_decreasing_popularity() == 
    assert not pre_order_by_decreasing_popularity() == 
    assert pre_order_by_decreasing_popularity() != 
    print("La fonction pre_order_by_decreasing_popularity() est ok")
    
test_pre_order_by_decreasing_popularity()

def test_order_by_decreasing_popularity(network, group):
    assert order_by_decreasing_popularity() == 
    assert not order_by_decreasing_popularity() == 
    assert order_by_decreasing_popularity() != 
    print("La fonction order_by_decreasing_popularity() est ok")
    
test_order_by_decreasing_popularity()

def test_find_community_by_decreasing_popularity(network):
    assert find_community_by_decreasing_popularity() == 
    assert not find_community_by_decreasing_popularity() == 
    assert find_community_by_decreasing_popularity() != 
    print("La fonction find_community_by_decreasing_popularity() est ok")
    
test_find_community_by_decreasing_popularity()

def test_find_community_from_person(network, person):
    assert find_community_from_person() == 
    assert not find_community_from_person() == 
    assert find_community_from_person() != 
    print("La fonction find_community_from_person() est ok")
    
test_find_community_from_person()

def test_find_max_community(network):
    assert find_max_community() == 
    assert not find_max_community() == 
    assert find_max_community() != 
    print("La fonction find_max_community() est ok")
    
test_find_max_community()