"""
Дается массив строк, в каждой из которых закодирована следующая информация о пасажире самолета:

первые 10 символов - номер телефона
буква - пол человека
следующие две цифры после пола - возраст
остальные - его место в самолете

необходимо вернуть количество пассажиров, которым более 60 лет
"""


class Solution:
    # def countSeniors(self, details: list[str]) -> int:
    #     count = 0
    #     for i in details:
    #         if int(i[11:13]) >= 60:
    #             count += 1
    #     return count
    
    def countSeniors(self, details: list[str]) -> int:
        return (cnt for cnt in details if int(cnt[11:13]) > 60)



sol = Solution()
print(sol.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))