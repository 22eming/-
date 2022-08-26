import itertools
#순열
result = list(itertools.permutations(["1","2","3","4"],4))
#중복순열
result = list(itertools.product((["1","2","3","4"]), repeat=4))
#조합
result = list(itertools.combinations((["1","2","3","4"]),4))
#중복 조합
result = list(itertools.combinations_with_replacement((["1","2","3","4"]),4))
#리스트 내 모든 원소 조합
epoch_ = [500, 1000, 1500]
batch_size_ = [1000, 2000, 3000]
lr_ = [0.001, 0.002, 0.003]

result = list(itertools.product(*[epoch_,batch_size_,lr_]))
print(result)