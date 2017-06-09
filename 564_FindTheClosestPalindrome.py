class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        # reversed_n = n[::-1]
        # if n != reversed_n:
        #     result = ''
        #     for i in range(0,len(n)):
        #         if (i+1) * 2 > len(n):
        #             result += reversed_n[i]
        #         else:
        #             result += n[i]
        #     if int(n[0]) > 1:
        #         result1 = str(int(n[0]) - 1) + '9' *(len(n)-2) + str(int(n[0]) - 1)
        #     else:
        #         result1 = '9' * (len(n) - 1)
        #     if int(n[0]) < 9:
        #         result2 = str(int(n[0]) + 1) + '0' * (len(n) - 2) +str(int(n[0]) + 1)
        #     else:
        #         result2 = '1' + '0'* (len(n) -1) + '1'
        #     a = abs(int(n) - int (result))
        #     a1 = abs(int(n) - int (result1))
        #     a2 = abs(-int(n) + int (result2))
        #     print(a,a1,a2)
        #     if a < a1 and a <= a2:
        #         return result
        #     if a1 <=a and a1 <= a2:
        #         return result1
        #     if a2 < a1 and a2 < a:
        #         return result2
        # else:
        #     cho1 = '9' * len(n)
        #     cho2 = '1' + '0' * (len(n) - 2) +'1'
        #     if n == '9':
        #         return '8'
        #     if n == cho1:
        #         return '1' + '0' * (len(n) - 1) +'1'
        #     if n == cho2:
        #         return '9' * (len(n) - 1)
        #     tmp_result = ''
        #     if len(n) // 2 * 2 == len(n):
        #         tmp = n[len(n) // 2:len(n)]
        #         if tmp[0] == '9':
        #             flag = 0
        #             for i in tmp:
        #                 if i == '9':
        #                     tmp_result +='0'
        #                 elif flag == 0:
        #                     tmp_result += str(1+int(i))
        #                     flag += 1
        #                 else:
        #                     tmp_result += i
        #         elif tmp[0] == '0':
        #             flag = 0
        #             for i in tmp:
        #                 if i == '0':
        #                     tmp_result += '9'
        #                 elif flag == 0:
        #                     tmp_result += str(-1 + int(i))
        #                     flag += 1
        #                 else:
        #                     tmp_result += i
        #         else:
        #             tmp_result =str(int(tmp[0]) - 1) +tmp[1:]
        #         result = tmp_result[::-1] + tmp_result
        #         return result
        #     else:
        #         tmp = n[len(n) // 2:len(n)]
        #         tmp_result = ''
        #         if tmp[0]=='9':
        #             if tmp[1] != '9':
        #                 tmp_result = '8' + tmp[1:]
        #             else:
        #                 flag = 0
        #                 for i in tmp:
        #                     if i == '9':
        #                         tmp_result += '0'
        #                     elif flag == 0:
        #                         tmp_result += str(1 + int(i))
        #                         flag += 1
        #                     else:
        #                         tmp_result += i
        #         elif tmp[0] == '0':
        #             if tmp[1] != 0:
        #                 tmp_result = '1' + tmp[1:]
        #             else:
        #                 flag = 0
        #                 for i in tmp:
        #                     if i == '0':
        #                         tmp_result += '9'
        #                     elif flag == 0:
        #                         tmp_result += str(-1 + int(i))
        #                         flag += 1
        #                     else:
        #                         tmp_result += i
        #         else:
        #             tmp_result =str(int(tmp[0]) - 1) +tmp[1:]
        #         result = tmp_result[::-1] + tmp_result[1:]
        #         return result

        num_n = int(n)
        len_n = len(n)
        len_half_n = (len_n+1) //2
        half_n = n[0:(len_n+1) // 2]
        n_is_odd = len_n % 2
        num_half_n = int (half_n)
        num_larger_half_n = num_half_n + 1
        num_smaller_half_n = num_half_n - 1
        larger_half_n = str(num_larger_half_n)
        smaller_half_n = str(num_smaller_half_n)
        larger_n_is_odd = n_is_odd + len(larger_half_n)-len_half_n
        smaller_n_is_odd = n_is_odd +len(smaller_half_n)-len_half_n - (num_smaller_half_n == 0)
        def recover_from_half(half_num, num_is_odd):
            if half_num == '0':
                if smaller_n_is_odd == 0:
                    return '0'
                else:
                    return '9'
            if num_is_odd == 0:
                return half_num + half_num[::-1]
            if num_is_odd == 1:
                return half_num[0:len(half_num)-1] + half_num[::-1]
            if num_is_odd == -1:
                return half_num + '9' + half_num[::-1]
            if num_is_odd == 2:
                return half_num[:-1] + half_num[:-1][::-1]
        #print (recover_from_half(num_larger_half_n,larger_n_is_odd))
        num_r = int(recover_from_half(half_n,n_is_odd))
        num_r1 = int(recover_from_half(larger_half_n,larger_n_is_odd))
        num_r2 = int(recover_from_half(smaller_half_n,smaller_n_is_odd))
        print(num_r,num_r1,num_r2)
        if num_n == num_r:
            if abs(num_n - num_r2) <= abs(num_n  - num_r1):
                return str(num_r2)
            else:
                return str(num_r1)
        elif num_n < num_r:
            if abs(num_n - num_r2) <= abs(num_n - num_r):
                return str(num_r2)
            else:
                return str(num_r)
        elif num_n > num_r:
            if abs(num_n - num_r) <= abs(num_n - num_r1):
                return str(num_r)
            else:
                return str(num_r1)







print(Solution().nearestPalindromic('999'))