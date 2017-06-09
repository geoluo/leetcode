class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # import re
        # s_tmp = '100000000 +' + s
        # first_cal = re.search(r'(\d+) *([*/]) *(\d+)* *', s_tmp, )
        # while first_cal:
        #     #print(s_tmp)
        #     #print(first_cal.group(1), first_cal.group(3))
        #     if first_cal.group(2) == '*':
        #         cal_res = str(int(first_cal.group(1)) * int(first_cal.group(3)))
        #     else:
        #         cal_res = str(int(first_cal.group(1)) // int(first_cal.group(3)))
        #     s_tmp = re.sub(r'(\d+) *([*/]) *(\d+)* *',cal_res,s_tmp,1,)
        #     first_cal = re.search(r'(\d+) *([*/]) *(\d+)* *', s_tmp, )
        # second_cal = re.search(r'(\d+) *([+-]) *(\d+)* *', s_tmp, )
        # while second_cal:
        #     #print(s_tmp)
        #     #print(second_cal.group(1), second_cal.group(3))
        #     if second_cal.group(2) == '+':
        #         cal_res = str(int(second_cal.group(1)) + int(second_cal.group(3)))
        #     else:
        #         cal_res = str(int(second_cal.group(1)) - int(second_cal.group(3)))
        #     s_tmp = re.sub(r'(\d+) *([+-]) *(\d+)* *', cal_res, s_tmp, 1, )
        #     second_cal = re.search(r'(\d+) *([+-]) *(\d+)* *', s_tmp, )
        # print(s_tmp)
        # return int(s_tmp) - 100000000


        import re
        numbers = re.findall(r'(\d+)',s,)
        ops = re.findall(r'[+*/-]',s,)
        num_list = []
        op_list = []
        if numbers:
            for n in numbers:
                num_list.append(int(n))
        if ops:
            for op in ops:
                op_list. append(op)
        cur = num_list[0]
        flag = 1
        result = 0
        for i in range(0,len(op_list)):
            cur_op = op_list[i]
            if cur_op == '*':
                cur = cur * num_list[i+1]
            if cur_op == '/':
                cur = cur // num_list[i+1]
            if cur_op == '+':
                result += cur * flag
                flag = 1
                cur = num_list[i+1]
            if cur_op == '-':
                result += cur * flag
                flag = -1
                cur = num_list[i+1]
        result += cur * flag
        return result

print(Solution().calculate('1+2+4*4'))