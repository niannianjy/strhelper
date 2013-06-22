#-*- coding:utf-8 -*-
class strhelper:
	def __init__(self):
		return
	
	def between(self,s,l,r):
		s=s.decode("u8")
		l=l.decode("u8")
		r=r.decode("u8")
		l_index=s.find(l)
		r_index=s.find (r,l_index)
		if l_index>-1 and r_index>-1:
			l_index+=len(l)
			return s[l_index:r_index].encode("gbk")
		else:
			return -1


	def left(self,s,l):
		s=s.decode("u8")
		l=l.decode("u8")
		r_index=s.find(l)
		if l_index>-1:
			return s[:l_index].encode("gbk")
		else:
			return -1
		
	def right(self,s,r):
		s=s.decode("u8")
		r=r.decode("u8")
		r_index=s.find(r)
		if r_index>-1:
			r_index+=len(r)
			return s[r_index:].encode("gbk")
		else:
			return -1

		
	if __name__ == "__main__":
	print strhelper().between(u"是dad的sf",u"是","f").encode("gb2312")
	#print sb.trim("qwertyuiofds")