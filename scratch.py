url = "https://namegen.jp/?country=japan&sex=male&middlename=&middlename_cond=fukumu&middlename_rarity=&middlename_rarity_cond=ika&lastname=&lastname_cond=fukumu&lastname_rarity=uncommon&lastname_rarity_cond=ika&lastname_type=&firstname=&firstname_cond=fukumu&firstname_rarity=uncommon&firstname_rarity_cond=ika&firstname_type="
param = "country=japan&sex=male&middlename=&middlename_cond=fukumu&middlename_rarity=&middlename_rarity_cond=ika&lastname=&lastname_cond=fukumu&lastname_rarity=uncommon&lastname_rarity_cond=ika&lastname_type=&firstname=&firstname_cond=fukumu&firstname_rarity=uncommon&firstname_rarity_cond=ika&firstname_type="

# sex: male , sex : female

print({p.split("=")[0]:p.split("=")[1] for p in param.split("&") })

# 上杉 友里香,うえすぎ ゆりか
# 梅本 侑希,うめもと ゆうき

# json = [{"name": ,
#         "kana": },
#         ....
#         {"name":,
#          "kane":}]
