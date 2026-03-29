def solution(phone_book):
    def is_prefix(a, b):
        return b[:len(a)] == a
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if is_prefix(phone_book[i],phone_book[i+1]):
            return False

    return True