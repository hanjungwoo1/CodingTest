# from collections import defaultdict
#
# team_mates = defaultdict(list)
#
# team_mates["A"] = ["B", "C", "D"]
# team_mates["B"] = ["A", "C", "E"]
# team_mates["C"] = ["A", "B", "D", "E"]
# team_mates["D"] = ["A", "C", "E"]
# team_mates["E"] = ["B", "C", "D"]
#
# n = 5 # 사람 수
# k = 2 # 한 명당 최대 매칭 수
#
# # how to make candidates?
#
# #  A -> BC
# #  B -> AE
# #  C -> AD
# #  D -> CE
# #  E -> BD
#
# # 팀 순서대로, 정렬된 순서
# # result -> BCAEADCEBD


mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
print(new_list)
new_list = list(map(list, zip(*new_list)))
print(new_list)