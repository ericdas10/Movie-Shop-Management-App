class RentService:
    
    def __init__(self, repo):
        
        self.__repo = repo
        
    def add_rent_op(self, id1, id2):
        
        self.__repo.add_rent(id1, id2)
        
    def remove_rent_op(self, id1, id2):
        
        self.__repo.del_rent(id1, id2)
        
    def get_list_with_id(self):
        
        return self.__repo.get_list()
    
    def get_list_with_idmax(self):
        
        return self.__repo.get_max_rent()
    
    def get_all_for_id(self, id):
        
        return self.__repo.get_all_id(id)
    
    def get_all_for_id2(self, id):
        
        return self.__repo.get_all_id2(id)
    