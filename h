[33mtag V1.1[m
Tagger: 1230 <xjh_0125@sina.com>
Date:   Wed Jan 15 09:35:19 2020 +0800

release 1.1

[33mcommit 43baecdf5be8c5855dc44470d26388eb1dd358ca[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m, [m[1;33mtag: V1.1[m[33m, [m[1;31morigin/master[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: 1230 <xjh_0125@sina.com>
Date:   Tue Jan 14 15:54:24 2020 +0800

    替换后的字符串长度，滑动窗口

[1mdiff --git a/test/l424_characterReplacement.py b/test/l424_characterReplacement.py[m
[1mnew file mode 100644[m
[1mindex 0000000..49c57d8[m
[1m--- /dev/null[m
[1m+++ b/test/l424_characterReplacement.py[m
[36m@@ -0,0 +1,269 @@[m
[32m+[m[32m#!/usr/bin/env python[m
[32m+[m[32m# -*- coding:utf-8 -*-[m
[32m+[m[32m# @Author  : 1230[m
[32m+[m[32m# @Email   : xjh_0125@sina.com[m
[32m+[m[32m# @Time    : 2020/1/10 17:08[m
[32m+[m[32m# @Software: PyCharm[m
[32m+[m[32m# @File    : l424_characterReplacement.py[m
[32m+[m
[32m+[m
[32m+[m[32mimport bisect[m
[32m+[m
[32m+[m
[32m+[m[32mclass Solution:[m
[32m+[m[32m    def __init__(self):[m
[32m+[m[32m        """[m
[32m+[m[32m        给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。[m
[32m+[m
[32m+[m[32m注意:[m
[32m+[m[32m字符串长度 和 k 不会超过 104。[m
[32m+[m
[32m+[m[32m示例 1:[m
[32m+[m
[32m+[m[32m输入:[m
[32m+[m[32ms = "ABAB", k = 2[m
[32m+[m
[32m+[m[32m输出:[m
[32m+[m[32m4[m
[32m+[m
[32m+[m[32m解释:[m
[32m+[m[32m用两个'A'替换为两个'B',反之亦然。[m
[32m+[m[32m示例 2:[m
[32m+[m
[32m+[m[32m输入:[m
[32m+[m[32ms = "AABABBA", k = 1[m
[32m+[m
[32m+[m[32m输出:[m
[32m+[m[32m4[m
[32m+[m
[32m+[m[32m解释:[m
[32m+[m[32m将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。[m
[32m+[m[32m子串 "BBBB" 有最长重复字母, 答案为 4。[m
[32m+[m
[32m+[m[32m来源：力扣（LeetCode）[m
[32m+[m[32m链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement[m
[32m+[m[32m著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。[m
[32m+[m[32m        characterReplacement  正确 时间复杂度高[m
[32m+[m[32m        characterReplacement3 正确 On 滑动窗口[m
[32m+[m[32m        """[m
[32m+[m[32m        pass[m
[32m+[m
[32m+[m[32m    def characterReplacement(self, s: str, k: int) -> int:[m
[32m+[m[32m        if k + 1 >= len(s):[m
[32m+[m[32m            return len(s)[m
[32m+[m[32m        pre = s[0][m
[32m+[m[32m        count = 1[m
[32m+[m[32m        li_char = [][m
[32m+[m[32m        li_count = [][m
[32m+[m[32m        for i in range(1, len(s)):[m
[32m+[m[32m            v = s[i][m
[32m+[m[32m            if v != pre:[m
[32m+[m[32m                li_char.append(pre)[m
[32m+[m[32m                li_count.append(count)[m
[32m+[m[32m                pre = v[m
[32m+[m[32m                count = 1[m
[32m+[m[32m            else:[m
[32m+[m[32m                count += 1[m
[32m+[m[32m        li_char.append(s[-1])[m
[32m+[m[32m        li_count.append(count)[m
[32m+[m[32m        if k == 0:[m
[32m+[m[32m            return max(li_count)[m
[32m+[m[32m        res = li_count[0] + k[m
[32m+[m[32m        tmp_index = 0[m
[32m+[m[32m        for i in range(len(li_char)):[m
[32m+[m[32m            change_count, j, tmp, joinNext = 0, i + 1, li_count[i], True[m
[32m+[m[32m            tmp_index += li_count[i][m
[32m+[m[32m            if len(s) - tmp_index < res:[m
[32m+[m[32m                break[m
[32m+[m[32m            while j < len(li_count) and change_count < k:[m
[32m+[m[32m                if li_char[j] == li_char[i]:[m
[32m+[m[32m                    tmp += li_count[j][m
[32m+[m[32m                else:[m
[32m+[m[32m                    change_count += li_count[j][m
[32m+[m[32m                    joinNext = change_count <= k[m
[32m+[m[32m                    change_count = min(change_count, k)[m
[32m+[m[32m                j += 1[m
[32m+[m[32m            tmp += change_count[m
[32m+[m[32m            if j < len(li_char) and li_char[j] == li_char[i] and joinNext:[m
[32m+[m[32m                tmp += li_count[j][m
[32m+[m[32m            if change_count < k:[m
[32m+[m[32m                tmp += (k - change_count)[m
[32m+[m[32m                # print(111, li_char[i], i, j, change_count, tmp)[m
[32m+[m[32m            res = max(res, tmp)[m
[32m+[m[32m        res = min(len(s), res)[m
[32m+[m[32m        # for i in zip(li_char, li_count):[m
[32m+[m[32m        #     print(i)[m
[32m+[m[32m        # print(len(s), len(li_char))[m
[32m+[m[32m        return res[m
[32m+[m
[32m+[m[32m    def characterReplacement1(self, s: str, k: int) -> int:[m
[32m+[m[32m        if k + 1 >= len(s):[m
[32m+[m[32m            return len(s)[m
[32m+[m
[32m+[m[32m        def get_len(li, k: int) -> int:[m
[32m+[m[32m            res, tmp_k = 0, k[m
[32m+[m[32m            for i in range(0, len(li), 2):[m
[32m+[m[32m                tmp_res, k = 0, tmp_k[m
[32m+[m[32m                for j in range(i, len(li)):[m
[32m+[m[32m                    c = li[j][m
[32m+[m[32m                    if c > 0:[m
[32m+[m[32m                        tmp_res += c[m
[32m+[m[32m                    elif k >= 0:[m
[32m+[m[32m                        tmp = -c[m
[32m+[m[32m                        tmp_res += min(tmp, k)[m
[32m+[m[32m                        k += c[m
[32m+[m[32m                        if tmp > k:[m
[32m+[m[32m                            break[m
[32m+[m[32m                    else:[m
[32m+[m[32m                        break[m
[32m+[m[32m                if k > 0:[m
[32m+[m[32m                    if i > 0:[m
[32m+[m[32m                        tmp_res += min(k, -li[i - 1])[m
[32m+[m[32m                    else:[m
[32m+[m[32m                        tmp_res += k[m
[32m+[m[32m                res = max(res, tmp_res)[m
[32m+[m[32m            return res[m
[32m+[m
[32m+[m[32m        res = 0[m
[32m+[m[32m        tmp_s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[m
[32m+[m[32m        dic_sum, dic_index, dic_count = {}, {}, {}[m
[32m+[m[32m        for char in tmp_s:[m
[32m+[m[32m            dic_count[char] = [][m
[32m+[m[32m            dic_index[char] = [][m
[32m+[m[32m            dic_sum[char] = 0[m
[32m+[m[32m        pre, count = s[0], 1[m
[32m+[m[32m        for i in range(1, len(s)):[m
[32m+[m[32m            v = s[i][m
[32m+[m[32m            if v != pre:[m
[32m+[m[32m                dic_index[pre].append(i - count)[m
[32m+[m[32m                if len(dic_index[pre]) > 1:[m
[32m+[m[32m                    dic_count[pre].append(dic_index[pre][-2] - dic_index[pre][-1] + dic_count[pre][-1])[m
[32m+[m[32m                dic_count[pre].append(count)[m
[32m+[m[32m                dic_sum[pre] += count[m
[32m+[m[32m                pre = v[m
[32m+[m[32m                count = 1[m
[32m+[m[32m            else:[m
[32m+[m[32m                count += 1[m
[32m+[m[32m        dic_index[s[len(s) - 1]].append(len(s) - count)[m
[32m+[m[32m        if len(dic_index[s[len(s) - 1]]) > 1:[m
[32m+[m[32m            dic_count[s[len(s) - 1]].append([m
[32m+[m[32m                dic_index[s[len(s) - 1]][-2] - dic_index[s[len(s) - 1]][-1] + dic_count[s[len(s) - 1]][-1])[m
[32m+[m[32m        dic_count[s[len(s) - 1]].append(count)[m
[32m+[m[32m        dic_sum[s[len(s) - 1]] += count[m
[32m+[m[32m        for key in dic_count:[m
[32m+[m[32m            if dic_sum[key] + k <= res:[m
[32m+[m[32m                continue[m
[32m+[m[32m            tmp = get_len(dic_count[key], k)[m
[32m+[m[32m            res = max(tmp, res)[m
[32m+[m[32m        res = min(len(s), res)[m
[32m+[m[32m        return res[m
[32m+[m
[32m+[m[32m    def characterReplacement2(self, s: str, k: int) -> int:[m
[32m+[m[32m        def get_index(s):[m
[32m+[m[32m            tmp_s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[m
[32m+[m[32m            dic_sum, dic_index, dic_count = {}, {}, {}[m
[32m+[m[32m            for char in tmp_s:[m
[32m+[m[32m                dic_count[char] = [][m
[32m+[m[32m                dic_index[char] = [][m
[32m+[m[32m                dic_sum[char] = 0[m
[32m+[m[32m            pre, count = s[0], 1[m
[32m+[m[32m            for i in range(1, len(s)):[m
[32m+[m[32m                v = s[i][m
[32m+[m[32m                if v != pre:[m
[32m+[m[32m                    dic_index[pre].append(i - count)[m
[32m+[m[32m                    dic_count[pre].append(count)[m
[32m+[m[32m                    dic_sum[pre] += count[m
[32m+[m[32m                    pre = v[m
[32m+[m[32m                    count = 1[m
[32m+[m[32m                else:[m
[32m+[m[32m                    count += 1[m
[32m+[m[32m            dic_index[s[len(s) - 1]].append(len(s) - count)[m
[32m+[m[32m            dic_count[s[len(s) - 1]].append(count)[m
[32m+[m[32m            dic_sum[s[len(s) - 1]] += count[m
[32m+[m[32m            return (dic_index, dic_count)[m
[32m+[m
[32m+[m[32m        def get_count(li_index, li_count, end, begin):[m
[32m+[m[32m            index_end = bisect.bisect_left(li_index, end)[m
[32m+[m[32m            index_begin = bisect.bisect_left(li_index, begin)[m
[32m+[m[32m            res = sum(li_count[index_begin:index_end])[m
[32m+[m[32m            # if index_end == len(li_index):[m
[32m+[m[32m            #     pass[m
[32m+[m[32m            # elif li_index[index_end] != end:[m
[32m+[m[32m            #     if li_index[index_end] + li_count[index_end] >= end:[m
[32m+[m[32m            #         index_end -= 1[m
[32m+[m[32m            #         res -= li_count[index_end][m
[32m+[m[32m            #         res += (li_index[index_end] + li_count[index_end] - end)[m
[32m+[m[32m            return res[m
[32m+[m
[32m+[m[32m        if k + 1 >= len(s):[m
[32m+[m[32m            return len(s)[m
[32m+[m[32m        tup = get_index(s)[m
[32m+[m[32m        if k == 0:[m
[32m+[m[32m            res = 0[m
[32m+[m[32m            tup = tup[1][m
[32m+[m[32m            for key in tup:[m
[32m+[m[32m                if len(tup[key]) > 0:[m
[32m+[m[32m                    tmp = max(tup[key])[m
[32m+[m[32m                    res = max(tmp, res)[m
[32m+[m[32m            return res[m
[32m+[m
[32m+[m[32m        res = k + 1[m
[32m+[m[32m        for i in range(0, len(s) - k):[m
[32m+[m[32m            tmp = 0[m
[32m+[m[32m            if s[i] == s[i + 1]:[m
[32m+[m[32m                tmp += 1[m
[32m+[m[32m                continue[m
[32m+[m
[32m+[m[32m            # start = tup[1].get(s[i])[bisect.bisect_left(tup[0].get(s[i]), i)] - 1[m
[32m+[m[32m            count_c = get_count(tup[0].get(s[i]), tup[1].get(s[i]), i + k, i)[m
[32m+[m[32m            count_c = min(count_c, k)[m
[32m+[m[32m            tmp_res, j = k + tmp, i + k[m
[32m+[m[32m            while count_c > 0 and j < len(s):[m
[32m+[m[32m                if s[j] != s[i]:[m
[32m+[m[32m                    count_c -= 1[m
[32m+[m[32m                tmp_res += 1[m
[32m+[m[32m                j += 1[m
[32m+[m[32m            tmp_res += count_c[m
[32m+[m[32m            while j < len(s):[m
[32m+[m[32m                if s[j] == s[i]:[m
[32m+[m[32m                    tmp_res += 1[m
[32m+[m[32m                    j += 1[m
[32m+[m[32m                else:[m
[32m+[m[32m                    break[m
[32m+[m[32m            res = max(tmp_res, res)[m
[32m+[m[32m        res = min(res, len(s))[m
[32m+[m[32m        return res[m
[32m+[m
[32m+[m[32m    def characterReplacement3(self, s: str, k: int) -> int:[m
[32m+[m[32m        dic = {}[m
[32m+[m[32m        res, l = 0, 0[m
[32m+[m[32m        for r in range(len(s)):[m
[32m+[m[32m            dic[s[r]] = dic.get(s[r], 0) + 1[m
[32m+[m[32m            max_letter = max(dic, key=dic.get)[m
[32m+[m[32m            while (r - l + 1 - dic[max_letter]) > k:[m
[32m+[m[32m                dic[s[l]] -= 1[m
[32m+[m[32m                l += 1[m
[32m+[m[32m                max_letter = max(dic, key=dic.get)[m
[32m+[m[32m            res = max(r - l + 1, res)[m
[32m+[m[32m        return res[m
[32m+[m
[32m+[m
[32m+[m[32mif __name__ == '__main__':[m
[32m+[m[32m    sc = Solution()[m
[32m+[m[32m    s = 'CCDAEEEDDEBCCDBACFCEDFAECCCCFDEADFECCDEBBEAFEBEEAFDEACBCECEDFBBDECCAAFCDDCABDBAEFABCBAEDCBFAAECEECAEABCBCCABAABECAFEAACEEBCFFFDDCDBCDCACCFFBDBEDBDEDFFECDBDBDABBBDAEACEDFBBAFBABFAEBADCEFDEAFCFDDFFCAFAEEAAEEECBFADCEFADAEEADCBACCDDEFCCCACEBCCEEDBBFFBCEDEFEACBDBBABDCBADDFEADCBEBBCFBCBAECECCCDDADCDBEAFCEADEBBFFACEAAFFDDCEFEEACDFDACFCEAFDCABBBBEBEBDDABEDCAEFCBFEFFABBCFAFCCBDECDBCABFABFABEECEDFFDFFDEBDBBBEEAEFFEDBADAABEEACFCCBEDADFCBDBDDBDCABDFCDECEFBFDFCDCFEBCCDDFABCBBCCCBCABEECBCBCBEADECAFFFCFAEFFFCDADBADFDFFDCBABFADFAAEFBADCCAFEEBFCFEBCFCEDACCADAAEEEBDCADABFBADBAECACBEFAECFFBCFBDEAECEBCFFDCEEEEEAFEBFFAEBBBDBBFFDBFADEECFDEBDBBCEEDBBADDBBDEDDAFEBCEDCAEBEEEDCFEDDACCDDCAEFDECBDCBBEFCFCECAABCFBBACACCEACDCBDBFECBDFFEBBFBABDECAECAFEEDAABEAFBECAACCACEEAADCEFEEBFFCCBDBCCBADDAAAADBFAECFBFACFDECFACDCCBBCADAEBEDDEEDCBDAFDDAAAFECDADBDAACCBDFAEEACFBBDEDDCCEAAEFEBFCAAEDDCFBDEFECBEFACCCDEDAAABEDAECDEEFCDACCBCDFBCADBCFAACCBBDFFBFBCACEABACAFEDCECCBDFAEDCBDCBAAFEDBCCBBFAFAEABFBEEBDCDFECDDDBDDCCBEFCCEDCECFCBEFFFBFBFBFDDCBEDADECCFFAFAEBEAABECFECABDABFBCEDFCCCCADEBCFBECCDFAAFEFEADACDEFFCBACAACFFECAAFDEDECCDFEDADBDAECDFFECAFFFEDEBEDBBBBBABDAEFFFDDDDCCEEEADEBFEAEFDACBFDBFDADEEACECFADACEEDBCECBCEFCBFBDEADAFCDACCFAEFEFAFDFECAABACFFFDCCBBCCDFECEDECDFDBBFACCDFBADFABBFADDFFCAAABEBDFAAEDAACFCCAEECCAFCEEBEEBCCFFEFFDEFBEEFBBFECFADAFFEBAAFBCFBAFBACDFDAEDBEBEEBBFDEDCEFCBBBABCDAEBEFAEBEAFDECABBADBFCEFFFDBAFDBBEBBCAACBFDDCEFEEEDDADBCFCEAACDBFBFDEACDCDFABDACBCAEEDECCDBDBCBACEBBBBADCBFCDDBDFECEECFDFFBDCBAAEBFCFCDFDBBBFCDECBADAFCBFECABACBFDBAFDCDBBBECCDFDFBECEDBCCAEFDAFACEBFDBDFAFCFFACABCAAECCBBEEBDAFAEFFFEBDECBEAECEAECACDBCFEAADBFEADCCEFAFCAADAEEDFBAFACBAFCEACAADDECFBFDBFCCFAABDABFBEEDFDBAFFECBDDCDCBDEBEFDCCBDBFECBFEAFDCDECAFEAAEAABDFDBBFECAECFEBADCFEEDCBDBFDBBECECFBDDBEFAACEABEFCAAFBDACDDFAEEFDAACBEAEAFDAFEECEFECFBABABBCCBFECBBCAFDCEDCBCAEBFBBCCCBBAEFEFBEEDEFCABEFEECCFBAADEFCEFDDDEDDDBBDABEEFECAEEBCCDDFBAEDCBCCEFFBECFBDECAFEEDBECEBACEBFCEFBECEDFABFAADEBACECDEEBDDFAAEFCCFBFCCAEAAEFAEDEEFBADFCDCFAFEDBDADCFFBDBBEDFEDEFDFCAAAFBADDBDCCCCACDDBBFBECCACDAACCBBDFEEBAACAEDEBBDCDEBDADCAADEFFDDAEADDDFBDBAACFDCEEAAAFDEBBFFEBACADCACDEECCCABFDDCAADEAFABCCCEEFEDDDCBEEFFEDFBBAECDEAAADAECEAACBCBBFCFBEEAFFFDEFDDCBDDDAFAFDEBCEEEACACACCBBBCBADDCECBDEDAAADEFDDDEAEBBBEAEFEEBEAABCFCBCAFDCFDDCFDFAABEFCAFEFADBCDDEADEFAFDAFDECBCECEADFCDAECBDBFEAEAACEBFFFAFEEDABBEBCCBAFACEAFFFABCAEAFEDFCBFEAAEDCCBDBFEFFFCDEAEBEBCDCDEEFDBEEAFBBAEEEAABBEDBFACFCACFABAEBAFADBBEBCEBCFECBFDABBAAEDCDECEAADEDBBFAEECCADFCBAFAAFEDAEFDACBDEAABFFAACEFDFCFFCEFACFBDDABCACACDACACDEBACDCDCADEADFBFACEAABCFDCDDAAEFCFEAFCFFAFDCFDEDAEFCEDAFDFFFBECCFEAADEFAACFDEFBEEBCDADDFCDBADBADFFCCCFBBBDDDEEADDADEFDDECFFACCDFCCBBFACFDFBBEFBCEDACACBAECDECBCBCCFEBEEAEECDCDBAADEABFFCFECBBEFACDBFEBAAFBBDFDEEFCCCFEBBBFECCEBDBADBFCDFCDBADCEACCBDCBAAFEEDDFEAEDFEEEEBCAFCDDBCBDDDCABCBFDCBEFCBCEBFDFBCCDBEAABEAFCACDEBEDCAADEDDFFBFEDAFEFACDDCAECEAEBBECBAACADDCBEAFFBCFAFBBAFCDDCEBCAEFEFBABFCBFDDAEFDBFCDFDACFAAAFCECEAEDDBFFBBBEBAAAAADABEDEEBCECCBCBCEEBECDCFDCCDEADFBDACAFFAADCBDAEEABEDBBADAEFCBBAEFEDBBFEAADFAFBABADBBDCDECCDAEBFACDDEECEEBEFFBCEAEDEBDEACCFAEDDDFADCCFDFACFECEFDDCCEECBFDABDFDCBEDDABEFFCDDEDCEBEFAEBFCFBEACCDABDDACBEFBCFCEEEEFEBABBEFCAEEECEBBDBEBDDABEBCCABCFFCDBBAEBBFAABCEBADCCEEADBBEBCCDBAAAFBFBCFFACCFFFDDBFAAEBACACFEBEDACAABAEECFCAABCDABBCEDADFFAABBDDBFDCFEEFADBCCBDAAFCFCBEAECEBFFEDDFCBCCFDEEAABCDFEBFEACDAFCCDCFBCDDAEDFBAAFBCDFFBAAFBCEFAFCBEAEECEDDBBDFFDAFBBFFECAFDAAFDCFDCBBBFCEDCFADFAEEDFEFDCCACACAACCBAEDFDDBEECFDEBFCACBDACBAFFCCEDBBEECBACFCDBEEBAADBCABCFFAFFCBABDBEBCDDEEDEBBDECAEEEBFFFEDFDFECEAFAADDAEAAAACBBDFFACAFFEEFAECDDFDBCBCDEFDFFDDACEEBBFDBBEBAEFDACEEEACAFACCBDFEABEDCADFCFFEEBFFBFAEAFBDEDABEACADEACDDADCCFBCDBFCBDCADBFBBBFECCCEBFDEDEEDBCDCBEEBCEFFEADDFDCABAAEAFCAEACCBDFCEECDCFCABCCDDAFDFACCCFBDCFFFDDBAFCECCCBFCAECABCBFEEDADCFFCFBDAEEDBCABBCFFDBCECBAABEEFFDDAFDEBAAFBDBDEEBACFAEBEECFAEDDFDBBFEDACBADECEBCFCCFCCBEEEBCCFFFEFFAEDBECAFBFBFDDFEBDCECAFFCCBAECCAAFEDDDAFAABADBAFEDAFFEEAFFFBEFBEADEDDFAFEBDFAEBCDDFBCFEEAFDDAAFAAEACBCEACBCBEECFAAEFBBBEFDBBDDCEBBABFEFCABEBDAFDDDFDCCFFFECDFACCAABCDABDABFFBACBAADDCEBBBDFEEFAAADEEEFEDDDFCBCDFDFEFCEEFCBCAEFFCEDAADBDEFEABBEEDBFBECDCACAACCAAAFCEFBBCCEADBFBCFCCCEFABBDADBACACDABBADAFDECFBDABDEBEBFDFCBADAEDFCFFCEDEBBADFDBCFFBFAFDCFEADFFAEDFEBDCCEAABDBDCADABACCAAFEDDFCADAFDFADDCEEAFAAACAFCAAAFEBDBEBACCABCBFCCBCEDADAEAFDAEFDEABCACCCECFDFFCAEBCECAEEDFFEDAEFEBCAAECCFBDDACABCBCEBBADCDDECDBBEFAFCDAFBEDCEDBAEBCADEDFFEECEFDDEFCBBBBEDBBBBCBAEFDDEBDBCCEAAAFADEFACFBABCCFDCBBADCBAEEEEBAEAFCEEFBCFCBFEFDDCBDCDCEAFEAADEEADAEFBBEDBBCECABFCCEBADECACDAECEBECBAAFCBEABCBDFECDECFDBAFDBCBDFEDBEACDBDEBEABFBBEDDBAFBACCDEABDBEDEEFEDDDCDACEBEDBBBFBEFFBCAFBAFFAEAFACCFDFDFCBCDAABDFBBECBFFAABCFCFCAEEBFCCDFFEFEADBCDDDFCEDBFEABDDFBCBEABECBCCACCCCABAAFCABCAFFCCCFCBBEFEEBEECEEBDDEBABAFFEAAADACDFDBEAABFAECADAEBFFBECBEBCEEEBFEAECEEFAFAEFCDECDECFEBFFBAAFADCAAABDBCDABCAAAFBAEDEFFEDABCDBBECBCCDEFBDACFFBFCEAEFBDCADAEEDCBFEDAEEDBBFFFCFEDFDDAADDCAECBBECDDDFBAFEABFDBBBEEDBFAFAADFDCFCBEAFAEBBDDFDFFCBBCFCCBCCEBAFBAFDEAFCAFFCBDDABDFDBAFDEADCBDFCAACAEEFDEABAEDAFBBBFDACBDABFBFBEAEEFEFCCDCECAECECEABBEFABDFAFDABBDFEFFCBDFCFFEEBBFEDFCADDBEADFFDDACCDCDEBADDABBDADAFCACAEDFDFFDCABAABCCEBDEAFBDCBECFFCAAABBECDBFDFBDEDCACDEAADCDFEAEBBBADFECECEAEBEBFDCABEDDBEECEEDFCEDDADAEBCEEDBAFDFACDEDDABDEBDDDAECBFEFCEEDBBBEBADFFCABDFABFBBFCABFFCCADFCBFBABCDFFDCFBACBCCBBDCDCABFDAFBCFAFBDAFAACBFACCCDBEDFADFEEEDCADEFFFDDCECADEFCDEDCCDDFEDFEBCBCABDDFEADFDFFECFFCCBCABEFBDBDAEDACBBFFBDFEEEACDEBDFFCDEFEBFBBEFABBDFDADDBACEEEBAEECEDACCCDDDFBCEEECCDAEDCCCDBCEBDDADAACCFAEEDFBAEECACFFDEBADDDAABBCDACEEBEAFCADEAFFDBAFFEDAFECCAAEBAFACACEDEBCFFFFDEDDEAFEBCEFDCBCBCBCCBADBAACFDFFBFDABDACCBFEEADFECBBCAFCFDADAACFDBAAAEEACCDAFFCFBCAFBDBAECCCFBDFBFCEBEABFEADAADAEAABEDDACBCCDBAFCCFEAAFBBBBFFCBADEBDECFCCADDCCFFBEDCAADDDFDCFBABBEBBFFDDDBCDBCDDAEDFDBCADEDDECBAAAFCDACDEAAEFEACEBCEEAEBEFCEDEDCAAAFBFCDCEFFBCFDCBAFEDACCBFFAFCBADAEFDBDFAABABDCDABDEAAFEBFFCFABBDECEDDBECEEACCDBEEAEBEECDBBBDEEADFDEFDADDBAACBCCDCCFCFEFEBCDABEFBABCDCBFDAACDDFCCFACEBDCFEABACFEBAFECEAABFFDBFFFDACEAECBFDECFDAFCECEBCBFFAEDBEEDFDEBBBCFFEBFFDDCDBDFCCBADCDDBDEACEEDDBECCEFDAFEAABCEDFAEAFCEFDAAECEFDEDDBACDBDFCAECBEFEDADBBBDFFADDCCADBFBAECBACDDBEFDCEDBCFDDFCAEDBCBBDCFBDACFBBEEECFCEBFCFDCAACBBEBEACFCCECCCEFEAEBEBADDACCFCFBCADEEBCBDBFAAFEFBFBBAFAACDDFFBDCECAABEAADAEDCECDEDADFBEACDBBEAACDAABEEDBDADCACFEEABBCBFEDDCDBFDCADCABBECBBCCBDBFEBEBFCCEDBFABDCFFFECFCEEFFBECCCAAFBCBDBDDADCFCEDBEEDAEBCABDFEDFACBFCBEABEFCDBDCFACBBACDFEBCCDBBBCFEADACAEDCCFEAECDAACAFFDFFABFBDCBAEBABDBCFABAAFEFECBAFBCEDCFEAFEDCBCCDDDCEBDFADCEEBABBFAEEACADCABCFAFBBEAFDFBDABBCECAEFEDACCCAEFFACCDADACCFAFEBABACFEFACCAACFFFDCDDDADCEEAABEEBBEFFFBFEECFEBCBFDEBDAAFCBFABFFCBDBDEADACEACBCDCEEFABAFBDDADDADDDAEBDDABBEAFDEDFDACCCFEBCACDDEFBBDACCBCACBDFFCFAABEFFDBFAFDADBDFEFABEFFFCBDEBFDBEECDACFEDCBFDBFEABEEEBADBADDFEAECBCEBAEABBBEEFDCEFBDEADCFBBAFEACBDEDAAEBDABBAAFCBDEFDEABCAFCDECABFDAFBEEDDECBCABBACFEBBACEEEFADEDECFBABECECEBCABAAFBFDADFDEDCBEEAEEAFBFFCCAACCEBCBEEBBABBDAEBDBBEFDEDCABEAAADFCDFDEDFBFDFFDEEEBEACBDDDFDCACAAABBDBFDCDEDFDDFBDDABEFFBCCDFFAFAACCEACEFAEFFCBBEECCBDEADCDBDADEACBFFDFDFDACFDABBEFFDFEDEDEEACDFEEBFCBBDADAEEFFFBFDACBFDBBBDDDDCDFECBDBFAFDEEEDBFDBDEFAFEFDACBEDDAAEBEDCFCABFDAADFEFBACCEBEECECDDBCCDECFEABABEEDDAEBEDCEBABEBBFAEEBCEDEFCDBEEBBCBCEEEEFFFFEDFABFBDECFFFDDBDFCCDBFFDDDEDEBAEFABFCDEDCCDEBBAECCAEEFFFEFCACACDEECBBBBEFBAEFAAFBBCDABEDEEECBDDCFEDAFCFFEAAFEEFBFDCBDDEDBEFECBDFEBFEBDFDEEBCAEBDFDFAEAACEADCCECDECCDFAAFBCEDFEFAEDCFFDAECDAAEBEFEFDCBDCCDCDADBEDECADBBCBEBBABEDEEDEDBBAABCCBBABADEADFCCFDBCACAAFAFCDDFDFFAAAFDFFBDDEFAFFFCAEEEFFACECEDDEDCEFACFEDBDDFABEBFCEBECFFACACAFFBDBCBDBFCEFBDFBEFAEDFCFBCDCCABFEABECFCACBEFFAEAAAEDBFAAEDECBBBEAFDCACDCFDAFCECBCBCCEFFDCACDEEADAADDACCDAFECDFAEEFCDBAEAFFCDBADDFAAFACFEDDADBDFECAECBCFCAEACDDFEABFFEDADCECDFADFCBDFAFCFFEFECABACADCFCCFCDFDFBBCEFDACBBCCDDBADEDDFBACFFAFBBFBECBCCFEBCFABBBDCCCBDBEBDDCBBDFDDBEFCDADAECDEBFDCEDEBBECAABABEDAAECAEEFFDDFBCADCFFCAFCFECFCEBFDECBEEBCCFCCACFAFEBBADAEECCEEECBBDAEEEDCCDCECAEFBAFDABBECFDFBDEFDFAFDEABEFBAAAACCEAFEFABAAEEAAFABFAACBDCCBDFCEBBECECFEBCEBEFACCFEEBDBAEBDAAFBFFBADADECCABFEEABADEFBBFFEFCFFDEEDECAECABBBAFAFDCFCDADACACDDDBFADBDCEADEAAAACDBDADCCEEEBBFADAEEEDABDCEACBBEFEFEADBDEABEEFABDAFBFAEBBDDFCECECDFBEBFBFBCCBABBBAFDBECBADBACDBAACDEBDFFEDEBCACACADBCFEEDDCFBCABACAADCDAAFEADEDDBCCDFFFCAEAFBEBBCEFCEABCCEBBAAFCCDDFDEBEAECEEADDADFDFADDAABDCADEDDAACFCFADDCEDBDCAEFACFBDADECCCFDEFFDCADDEAACFCCEADCAEECCBAABFBDFADDDBBFDDCAEDDBFCCEBFADFBAFCBEECEAFBFADEBCCADCAAEDCCCFACECDADFAEDEBDDAADBBEECEEFEFEEBDBBBACBBBEEFECEFDAAFEDECCAEABCBCAFBFABFBAFDCDEFDDFFCADBDABFEFCCBDEEFBEDDBABACABBAABCBCBCEDAAABFABFDFAACCFDCDFFCFBAFCFDECEBBBBCFEAFABDEDEBECCCDBEABAAAFFEBAFAEDDBEFAFCBAACCABDCCCEFADFCAEFBFABBBECFCCFDCFDDCECFFCBDACCDACDEAEDFCDADCDDCEBCBEBDDAEBBEDDDCBBEBADECCFEAABFDDFECCCCCDEADFBAACCBAEADBDADFABCDDCECDFEDBFFBDFDAEECDBBAABAAFBECFCDDCBFDBFACDBACAFEBFBFFEEDBEABEFEBABDFBBDDEDFABBDBFAFBEAFAEDCABCFCDEFABAFDDABBDAADCEBACEAEADBEBCBBDAFABCEEEADFCABFFCBFCBACEBEACEAABDCCAFFDABFADDCFBDDAFFABAEDADFFBCBABDCDEACCDAAADEAEDEBFDDBADDBACDEABFFCAEBEBDCFDABACECFBBFBEACCDACBDBCEECFFAECEBADEDDFBEEACECBAFDBFFAFBBDCCCEACEEACFABECDBBAAFCDABFADFFACCFDECAFDCEFDDBDFBAFAEBEFEADFCFBDEBCACDBEFDEBAACCADFDDFEDEABBDDAEEADEBDFEBAFDCBCBABCDBAFBCDDEEDDCCEAFFCCADAEDFCAFABEDFECFBBAEEABBDBECCCCCEABFFFBBBFBEDDDEAFFFEAEFFDAADDEABEDDFDBBEFABFECFEECCCCDBAECFCEACEDEBAFCCFDEDCFCCDBDEBCCFBFACCDDAFFBCDEAFEEDCDABBFEAADDECDBFBBFAEDAACABEFFFFECFADEEAEDEEEDFFBCBFABEDABBDBBEDBFEEAAACFFDBBDEEBBBDDDCCEBBCDDFEEFDFBFCBCEFEDCEFFECCBDEEFFECABFACBFCFFEFAECDEABAFECEDEEBAFBBCFFBDAACFBCBFBEFABBBCECCDAACBFBAEABCBBEFEFCDDBBAEFEFBDBAECDBCEAFECEDDECAFAEABCCEAAEACEFFFADDCDEBFDAAACFCCEBEBABCFBDDEECEDBFFFADBDFABDFFCEDCAAEFCDCFECBBCCCDAAABDBAECBABDABEAAFABBFFCDECFCAEFCAFEECBFCAEDCFFDBBFDEBBCBCFBFFFFFECDBEFDEEDFBAFADBBBFFEEFFECFEEEDABBCBDEDEFDCBEBCCAEFFADDAAECCEFEFCFADBAADAFDEBBEECABDEEDCEBCABFBCECDDCCDBBABDABCEDBDCBBDDACECBDEFBEEEEBACBBADFDBACDCDCEBFDEBDAAFCDDBCCCBACAECCAADFBCBACBFBDFFCCCAFBBBBACEFABBEFAAFFDCEEDDDDFBBBADDEEDFBFADCDBDAAAEEFAFFAFCAACFCCFFDAFFCCDCECDEBADACCFFEBCAFAAFBB'[m
[32m+[m[32m    k = 4567[m
[32m+[m[32m    # s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[m
[32m+[m[32m    # k = 5[m
[32m+[m[32m    # s = 'ABAB'[m
[32m+[m[32m    # k = 2[m
[32m+[m[32m    # s = 'AABABBA'[m
[32m+[m[32m    # k = 1[m
[32m+[m[32m    # s = 'AABA'[m
[32m+[m[32m    # k = 0[m
[32m+[m[32m    # s = 'IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR'[m
[32m+[m[32m    # s = 'SSMESSTR'[m
[32m+[m[32m    # k = 2[m
[32m+[m[32m    res = sc.characterReplacement3(s, k)[m
[32m+[m[32m    print(res)[m
[32m+[m[32m    res = sc.characterReplacement(s, k)[m
[32m+[m[32m    print(res)[m
