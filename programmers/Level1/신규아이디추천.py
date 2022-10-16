from re import sub
def solution(new_id):
    new_id = new_id.lower()
    new_id = sub('[^a-z0-9-_.]',"",new_id).strip(".")
    new_id = sub('\.+',".", new_id)
    if new_id == '': new_id = 'a'
    if len(new_id) <= 2:
        for n in range(len(new_id), 3):
            new_id += new_id[-1]
    if len(new_id) >= 16:
        new_id = new_id[:15] ; new_id = new_id.strip(".")

    return new_id