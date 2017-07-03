import heapq
import bisect
from collections import deque, defaultdict


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # brute force is faster than heap?
        result = [[k, h, k] for h, k in people]
        cur, n = 0, len(people)
        last_h = -float('inf')
        while cur < n:
            theMin = result[cur]
            idx = cur
            for i in range(cur, n):
                khk = result[i]
                if khk[1] <= last_h:
                    khk[0] -= 1
                if khk < theMin:
                    idx = i
                    theMin = khk
            if cur != idx:
                result[cur], result[idx] = result[idx], result[cur]
            result[cur] = result[cur][1:]
            last_h = result[cur][0]
            cur += 1
        return result


        # the best solution, lower element's position can not influence
        # the higher's k
        res = []
        for hk in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(hk[1], hk)
        return res


assert Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

import time
# tic = time.time()
# print(Solution().reconstructQueue(people))
# print(time.time() - tic)
tic = time.time()
Solution().reconstructQueue(people)
print(time.time() - tic)

people = [[798203,182],[688411,102],[350826,271],[85739,176],[180601,758],[592431,38],[155633,150],[963524,12],[110508,80],[179830,256],[592290,313],[272888,376],[851172,20],[522791,384],[733429,201],[300961,264],[380367,574],[901984,60],[737459,136],[513994,305],[345135,339],[538049,73],[89174,678],[86480,255],[610391,360],[558022,431],[298730,398],[586048,420],[175571,273],[289773,605],[680130,275],[597582,96],[618790,301],[367734,253],[273655,550],[942212,48],[645818,97],[885055,105],[98739,23],[934702,37],[19278,86],[159487,809],[943171,21],[983567,10],[560305,353],[528508,425],[11703,835],[852004,104],[641402,64],[626005,170],[941036,18],[406904,9],[1206,124],[520269,417],[195123,409],[684921,114],[324025,624],[44101,425],[274432,674],[16001,977],[406332,525],[471994,437],[792346,49],[412433,437],[376898,529],[602881,325],[707847,278],[820993,112],[231367,83],[698506,202],[898111,37],[543455,123],[275860,314],[275515,502],[329528,497],[532892,403],[715489,227],[579791,339],[915209,4],[83031,227],[874455,19],[447534,126],[408990,97],[279239,51],[895675,61],[39908,655],[779111,225],[839949,140],[652312,347],[601241,173],[389733,534],[888611,27],[928843,26],[262583,693],[886105,16],[586903,69],[149832,642],[189291,24],[340773,69],[582664,321],[229329,382],[879519,63],[958996,34],[243767,344],[818955,152],[173332,430],[713814,192],[531794,168],[80886,862],[619592,156],[505905,421],[436388,553],[363565,371],[502484,67],[52927,124],[430275,61],[892379,36],[412173,377],[390852,97],[808927,105],[116840,500],[742367,97],[357308,227],[806051,18],[381652,386],[669161,307],[971017,7],[142838,346],[742675,209],[414583,360],[950088,39],[697247,193],[400735,542],[761981,136],[390979,90],[895669,63],[13540,966],[599402,185],[302059,330],[158547,198],[183745,169],[84542,293],[495924,287],[479186,249],[340448,557],[925566,20],[506685,287],[138715,410],[944095,11],[19420,807],[851013,77],[202235,351],[862565,82],[648989,281],[15781,828],[242006,566],[605841,357],[80254,448],[168754,685],[811272,96],[697147,166],[756256,15],[655788,60],[25861,60],[601157,287],[463952,512],[916418,67],[850343,149],[618770,260],[606994,95],[769567,161],[842299,46],[656132,240],[714926,175],[850627,19],[370120,634],[422891,99],[566592,252],[707757,87],[923237,45],[829357,145],[102501,115],[532949,155],[925790,35],[753642,116],[609000,56],[29215,200],[232325,638],[327407,608],[810042,173],[469184,184],[826460,97],[141247,295],[11351,27],[566586,151],[621380,237],[388337,432],[543001,108],[837643,125],[355230,83],[573191,9],[82466,91],[872672,60],[127179,750],[955972,8],[997339,3],[163438,12],[876130,29],[651787,149],[807222,134],[405350,102],[386922,451],[713943,203],[777918,202],[458889,544],[837568,116],[476780,541],[350731,44],[760793,80],[148604,741],[849808,100],[750753,166],[9431,345],[331784,309],[722593,232],[525963,13],[376671,473],[499465,73],[250649,632],[92351,419],[739405,179],[103030,612],[60642,812],[400443,190],[406422,289],[884942,66],[924221,46],[262431,622],[700216,111],[392739,32],[755563,96],[82539,127],[564182,151],[24776,473],[215264,458],[599919,318],[188170,540],[372618,270],[778017,197],[860542,122],[973021,18],[459473,31],[128526,21],[336672,7],[256271,345],[17630,915],[826801,124],[733237,178],[753203,12],[269508,10],[742793,47],[895807,23],[598457,391],[531738,136],[810673,162],[423739,203],[547534,421],[162652,570],[33915,353],[852795,126],[332060,405],[30183,840],[825630,178],[90960,657],[140875,436],[82379,538],[4062,279],[710819,169],[147774,774],[758116,176],[670801,202],[462857,50],[600940,143],[979716,14],[110174,458],[406543,410],[722895,33],[983411,19],[786528,7],[490061,228],[60498,435],[647278,263],[805258,150],[581734,259],[837342,50],[382427,471],[994550,2],[438038,314],[682823,131],[37876,448],[301167,550],[165203,386],[858606,55],[873340,26],[997827,2],[444036,268],[594767,22],[591752,86],[336255,63],[863821,126],[299706,607],[846768,76],[666501,61],[573876,165],[977882,3],[163767,156],[210224,273],[711873,5],[691430,206],[264360,383],[611256,117],[686583,4],[858908,76],[455411,53],[742588,185],[156217,377],[594374,38],[678859,125],[66681,774],[405211,441],[136907,362],[153006,297],[640550,56],[784154,8],[51333,193],[965196,0],[568974,307],[273865,597],[425785,545],[313220,524],[887198,10],[206781,721],[919770,65],[582023,14],[52630,247],[873802,95],[388310,136],[736763,113],[715985,218],[622652,44],[8292,350],[434309,343],[198483,584],[413714,358],[337227,260],[670719,194],[51019,202],[587942,5],[684099,106],[558184,325],[532448,328],[150508,639],[46588,9],[940910,11],[87710,353],[361464,450],[47928,202],[138651,738],[942085,10],[256477,687],[718873,100],[314281,697],[457512,137],[504598,21],[505642,415],[909618,51],[246831,372],[526035,278],[847027,117],[383561,626],[760494,159],[356489,620],[279082,131],[634882,196],[692035,229],[374817,344],[667998,273],[485179,496],[900004,88],[881600,28],[610747,224],[735306,16],[673627,175],[835607,148],[786772,18],[772124,135],[819949,190],[179911,781],[476845,13],[882893,2],[985672,3],[740449,237],[961997,24],[206766,57],[534194,30],[817034,45],[905605,38],[136977,34],[660286,216],[535128,164],[65965,615],[683220,295],[388584,495],[603565,120],[411266,181],[769166,91],[199086,637],[306879,87],[328187,350],[890698,9],[931185,33],[575765,288],[187079,250],[250819,352],[66064,374],[994110,7],[880163,20],[150654,23],[31639,338],[753884,110],[56699,475],[291161,539],[139784,556],[800308,202],[102675,428],[327084,379],[32101,728],[321787,64],[73627,635],[907736,16],[185143,658],[493790,272],[693409,312],[718942,79],[58218,228],[280526,196],[361677,623],[979865,16],[707034,119],[227440,246],[261050,740],[501163,315],[916074,12],[623293,231],[498481,385],[170269,100],[562992,81],[616094,187],[371971,109],[744169,60],[264014,297],[520295,331],[908160,60],[445259,543],[391076,169],[236486,535],[913901,80],[249610,367],[937673,47],[877014,106],[883666,106],[457220,310],[263421,594],[45042,126],[961353,4],[955051,8],[364616,499],[532031,423],[678506,263],[408135,288],[53762,184],[830235,35],[936515,32],[880941,49],[497857,459],[987953,10],[687297,317],[898752,21],[325695,562],[299774,197],[541201,456],[948004,42],[198752,553],[283437,232],[856424,51],[720766,183],[855869,98],[42122,734],[34821,362],[549016,24],[790986,98],[998876,0],[67223,806],[42856,723],[192209,597],[266659,666],[769350,176],[892498,38],[574872,91],[89965,313],[592595,169],[64049,249],[72485,270],[41768,646],[344023,531],[660104,4],[919225,38],[300712,468],[824807,3],[876723,106],[786338,34],[812972,100],[271908,405],[162051,521],[989605,0],[869397,65],[969907,4],[813720,128],[681876,287],[525187,98],[413934,147],[336829,311],[806760,3],[352604,156],[395173,358],[288777,515],[17881,259],[577718,399],[190428,417],[987739,12],[447374,54],[996828,1],[856841,126],[935396,58],[264398,365],[127369,498],[349737,213],[344903,43],[585745,198],[587600,115],[546412,389],[757944,238],[718567,126],[986754,14],[663249,186],[756623,228],[845528,61],[351072,634],[838847,5],[426428,135],[665385,97],[613134,1],[802689,4],[824910,103],[542732,457],[489644,406],[808274,65],[458209,250],[66805,705],[738089,114],[605494,242],[187956,764],[177751,115],[364920,655],[498415,414],[536186,183],[691704,157],[79322,50],[68818,104],[902814,20],[395776,156],[348687,71],[138989,498],[479782,337],[591845,385],[939119,27],[430927,479],[145257,392],[115934,12],[374366,385],[436333,127],[485746,414],[456618,68],[870249,1],[33808,785],[527773,282],[539387,424],[981973,16],[324960,645],[448708,379],[481724,352],[190642,370],[32933,392],[772071,188],[481660,332],[150997,433],[937120,32],[779269,36],[666853,281],[829160,164],[734431,66],[464525,16],[844006,134],[106226,795],[884636,19],[253100,348],[591957,271],[264932,468],[653039,292],[53499,662],[177265,629],[680229,122],[205010,282],[254283,445],[669207,25],[652492,88],[665852,342],[644533,157],[716576,151],[937264,25],[67183,9],[627512,257],[680018,193],[321554,567],[958425,33],[887392,82],[225920,646],[657730,336],[961255,16],[788782,46],[52621,535],[29438,814],[602532,364],[809492,1],[398698,307],[466467,143],[861064,42],[716929,22],[289233,74],[92489,10],[101331,680],[198918,238],[546868,249],[616533,231],[932094,11],[713716,244],[185480,62],[710679,171],[493854,481],[630257,10],[521297,308],[423156,539],[104812,824],[823749,167],[434205,156],[918619,60],[532233,380],[695551,81],[919265,39],[867,477],[361647,53],[23591,8],[271173,614],[882112,82],[704136,224],[119446,288],[695190,195],[453361,52],[692780,80],[292267,631],[950177,19],[47775,575],[946291,14],[785739,219],[647660,47],[384719,157],[782340,30],[112818,453],[408935,575],[416219,420],[547451,180],[884396,59],[464777,394],[466146,259],[145207,668],[151121,701],[667394,314],[461918,88],[81815,483],[937987,40],[661636,272],[732120,146],[827267,183],[496664,304],[976653,5],[313871,5],[877502,121],[184662,761],[87997,462],[774064,89],[79841,197],[808780,169],[882679,6],[634982,297],[850772,130],[452352,62],[352683,369],[11016,812],[777667,4],[836767,51],[155624,592],[735552,11],[709520,53],[588011,197],[804212,66],[299142,538],[105473,15],[655607,93],[241427,583],[176347,667],[704617,208],[568591,271],[860279,97],[466483,346],[115152,857],[424865,521],[908490,50],[568295,38],[70757,332],[634855,141],[551045,392],[193785,298],[865319,11],[178665,681],[951680,3],[601412,193],[229780,286],[479138,465],[819743,72],[739205,172],[510094,313],[39960,504],[223437,13],[361823,199],[848021,146],[625769,95],[392059,97],[788789,11],[825105,125],[127513,596],[405070,535],[442949,350],[747271,22],[365029,102],[420235,591],[75076,89],[591844,81],[897652,44],[346115,296],[223820,410],[145494,355],[247452,399],[930490,60],[831979,113],[993731,4],[43453,81],[245400,495],[245786,230],[906021,22],[459833,263],[31224,121],[140068,552],[859551,111],[290021,521],[69883,82],[481274,11],[196637,752],[369028,273],[536879,465],[64,643],[398892,513],[252911,31],[313265,313],[379704,199],[680389,62],[7199,240],[908502,58],[821261,174],[987067,6],[717276,242],[890115,50],[227843,222],[655719,318],[44757,640],[409617,131],[36126,711],[900574,6],[158436,24],[564480,405],[300996,638],[40400,622],[962575,3],[184274,227],[743885,86],[591139,422],[452574,375],[393701,81],[215233,763],[858256,104],[699865,129],[870288,11],[66623,788],[271487,348],[914085,9],[40898,639],[401070,147],[903653,0],[654075,160],[701200,64],[628357,285],[39828,875],[914857,28],[858069,30],[256479,351],[989741,6],[241979,131],[402361,363],[509174,117],[981092,4],[80605,877],[472064,515],[180407,675],[886206,2],[696487,220],[745017,176],[681806,10],[719938,239],[840870,28],[46824,915],[986208,13],[100514,265],[240174,639],[500154,74],[766632,207],[280206,127],[552044,418],[836432,34],[985092,1],[70999,712],[163487,84],[473067,494],[222232,176],[126598,531],[10122,473],[137091,563],[183255,608],[830365,62],[666467,50],[228669,522],[581659,181],[665044,145],[652950,11],[577963,231],[833386,58],[927180,52],[19486,696],[555299,13],[160923,290],[856688,25],[254946,359],[726953,107],[905499,67],[796728,74],[483085,417],[262520,739],[785341,154],[564510,319],[848335,143],[562421,119],[156802,361],[375320,451],[576509,28],[867182,8],[189595,359],[505776,2],[35391,950],[628984,109],[973847,16],[175780,290],[804676,169],[379574,580],[607026,19],[682196,179],[224178,632],[906630,69],[316706,452],[704325,125],[337375,508],[416216,46],[659815,11],[577559,302],[70927,15],[528136,13],[403933,299],[207993,72],[868146,23],[435413,8],[256490,267],[825584,183],[461139,503],[777184,181],[23949,712],[610071,15],[464430,111],[630388,82],[182057,275],[843188,87],[958091,1],[183675,589],[488116,15],[865322,85],[720835,106],[134822,323],[255977,125],[155554,753],[999343,0],[118130,433],[524254,172],[557457,393],[209675,285],[415530,92],[329164,524],[332892,144],[910498,1],[863478,41],[659952,131],[238761,114],[486310,438],[733683,46],[513515,401],[626033,96],[436758,274],[167297,477],[815380,193],[995556,1],[629936,110],[76773,340],[183422,210],[446562,4],[22104,243],[897485,20],[448881,345],[117731,635],[311065,163],[285836,527],[368056,451],[546523,64],[843956,25],[346685,550],[210812,212],[214191,336],[772882,230],[529242,462],[443704,144],[631486,88],[213046,344],[756122,77],[695798,103],[944427,45],[505638,7],[226967,83],[460737,321],[582474,424],[504827,124],[590865,271],[635878,163],[552293,429],[209817,204],[792301,105],[444300,327],[509578,317],[234751,51],[32277,865],[160106,331],[193944,368],[156407,427],[811796,134],[961472,24],[583675,101],[67609,550]]
    # def reconstructQueue(self, people):
    #     """
    #     :type people: List[List[int]]
    #     :rtype: List[List[int]]
    #     """
    #     # dct = {(h, k): k for h, k in people}
    #     result = sorted([[k, h, k] for h, k in people])
    #     # heapq.heapify(H)

    #     cur = 0
    #     while cur < len(people):
    #         _, h, k = result[cur]
    #         result[cur] = [h, k]
    #         cur += 1
    #         lo = [cur, cur]
    #         for i, khk in enumerate(result[cur:], cur):
    #             if khk[0] > lo[1]:
    #                 lo[0], lo[1] = lo[1], i
    #             if khk[1] <= h:
    #                 khk[0] -= 1
    #                 j = bisect.bisect(result, khk, lo=lo[0], hi=i)
    #                 # import pdb
    #                 # pdb.set_trace()
    #                 result[j+1:i+1] = result[j:i]
    #                 result[j] = khk

    #     # while i < n:
    #     #     k2, h, k = heapq.heappop(H)
    #     #     if (h, k) in dct:
    #     #         dct.pop((h, k))
    #     #         result.append([h, k])
    #     #         i += 1
    #     #         for key in dct:
    #     #             if key[0] <= h:
    #     #                 dct[key] -= 1
    #     #                 heapq.heappush(H, (dct[key], hh, k3))
    #     return result
