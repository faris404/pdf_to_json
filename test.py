import re
 
email_regx = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
a = re.findall(email_regx,'dev.faris404@gmail.com fjgsajf burk.lee@gmail.com')
print(a)