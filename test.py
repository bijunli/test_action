import re
p = re.compile(r'(.*)(全部打勾|全打勾)(.*)')
a= p.match('全部打勾吧dsdd ')
print(a)
print('测试成功')
print('测试第二次')
punct = '！？｡。，？＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.?!,.~ '
result = re.sub(r"[%s]+" % punct, "", '嗯 好')
result = result.strip()
print(result)
# m = [1,2,3]
# n= 4 in
# inputlink = {}
# print('23','3' in inputlink.keys()) (.*)(满意|没问题|OK|不错|可以)(.*)
# ps= [[r"是(.*)",r"(.*)(对|按时|有)(.*)",r"^嗯$",r"^嗯嗯$",r'(.*)告(.*)时间(.*)',r'(.*)差不多(.*)'],
#                                                     [r"(.*)没(.*)按时(.*)",r"(.*)时间(.*)久(.*)",r"(.*)好长(.*)时间(.*)"],
#                                                     [r"(.*)没(.*)说(.*)时间(.*)",r"(.*)没(.*)告诉(.*)时间(.*)"]]
# for i in ps:
#     for j in i:
#         pa = re.compile(j)
#         a = pa.match('时间有点久呢')
#         if a:
#             print('******')
#             print(j)


