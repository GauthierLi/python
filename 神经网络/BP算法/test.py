# coding:utf-8
from nerve_net import *
import matplotlib.pyplot as plt

# # ----------------------------------------------------------------------------------------------------
# # test for plot
# X = list(np.arange(-100, 100, 0.01))
# Y = [NerveNet.sigmoid(i) for i in X]
# Y_1 = [NerveNet.sigmoid_deriv(i) for i in X]
# plt.plot(X, Y)
# plt.plot(X, Y_1)
# plt.show()

# -------------------------------------------example in MIC------------------------------------------------------
learning_set_rate_after_normalization = [[[1.8591818067303596, 1.1882793664888018, 1.6525211065906278,
                                           0.8483664440131231, -0.669673401883848, 1.7445444074872494,
                                           -0.7187306143990666, -0.029630442547297846, -0.11678881241348991,
                                           2.0821170158292337, -0.2729675076737704], 0.6], [
                                             [-1.5890265720550325, -0.5410789116684309, -1.6776956504775697,
                                              -0.5929988777907588, -0.669673401883848, -1.029906191162759,
                                              -0.9636791645978516, -1.9062251372095047, 0.3503664372404698,
                                              -0.6940390052764112, -0.2729675076737704], -1.0], [
                                             [0.41061938276572, -0.2503018560490732, 0.45037172059613495,
                                              -0.0287159872724378, -0.2796720337369327, 0.023682643767623975,
                                              -0.9636791645978516, 1.4716453131824676, -1.0510993117214094,
                                              2.0821170158292337, 0.9013078083567895], 0.3333333333333333], [
                                             [-0.9749620662439352, -1.0155046339947513, -1.0147807150193144,
                                              -1.0587976683670663, -1.0596747700307634, -1.0035664702894993,
                                              -0.22883351400149654, -0.029630442547297846, -1.0510993117214094,
                                              -1.1567316754606853, -1.0558177183608104], 0.0], [
                                             [2.3000486314152497, 0.6679414774857406, 2.365097794957029,
                                              0.5638135451729067, -0.4746727178103904, 1.726984593571743,
                                              -0.9636791645978516, -0.21728991201351852, 1.2846769365483892,
                                              -0.23134633509213706, -0.6643926130172904], 0], [
                                             [-0.534095241559045, -0.678815411698653, -0.5366499650166474,
                                              -0.6255454551857351, 0.11032933440998265, -0.7050496337258908,
                                              -0.47378206420028157, -0.21728991201351852, 0.3503664372404698,
                                              -0.23134633509213706, 1.6841580190438292], 0], [
                                             [-0.8017643851177283, -0.326822133843641, -0.9604092493483315,
                                              -0.4901698713603786, -0.8646740859573058, -0.6962697267681377,
                                              -0.7187306143990666, 2.5976021299797916, 0.3503664372404698,
                                              1.1567316754606853, -1.0558177183608104], 0], [
                                             [0.032733533035814034, 0.5608130885733457, 0.029703883769572406,
                                              0.7227702844442138, -0.2796720337369327, 0.4012186429510112,
                                              -0.7187306143990666, -0.029630442547297846, -0.5839440620674496,
                                              -0.23134633509213706, -0.2729675076737704], -1.0], [
                                             [1.57576741943293, 0.5761171441322592, 1.7213347663892868,
                                              0.7053263693342424, 1.4753341229241863, 1.0772714786980069,
                                              1.2408577871912136, 0.15802902691892284, -0.11678881241348991,
                                              1.1567316754606853, -0.2729675076737704], 0], [
                                             [0.12720499546829053, -0.5104708005506038, 0.42453181886778163,
                                              -0.361971507805233, -0.8646740859573058, -0.204594937133959,
                                              -0.7187306143990666, 1.4716453131824676, -1.0510993117214094,
                                              -0.23134633509213706, 0.11845759766974952], 0.5], [
                                             [-1.100924016153904, -0.2809099671669003, -1.1155709108681744,
                                              -0.2898710466449582, 1.670334806997644, -0.8455281450499419,
                                              1.4858063373899988, -0.9679277898784012, -1.518254561375369,
                                              -0.6940390052764112, 1.2927329137003094], -0.3333333333333333], [
                                             [0.4578551139819583, 0.3312522551896422, 0.4422581137659806,
                                              0.3641611089935319, -0.4746727178103904, 0.42755836382427076,
                                              0.016115036197288515, 0.7210074353175848, -1.0510993117214094,
                                              -0.23134633509213706, 1.2927329137003094], -1.0], [
                                             [0.2531669453782592, -0.47986268943277666, 0.29393777456341946,
                                              -0.44756866062642764, 0.3053300184834403, -0.055336518852154744,
                                              -0.9636791645978516, -1.155587259344622, 0.3503664372404698,
                                              -0.6940390052764112, 0.11845759766974952], -0.0], [
                                             [0.6782885263244034, -0.4186464671971224, 0.591032848669425,
                                              -0.5440687736520883, -2.2296788744715093, 0.26074013162696014,
                                              0.2610635863960736, -0.21728991201351852, 1.7518321862023487,
                                              -1.1567316754606853, -1.4472428237043302], -1.0], [
                                             [0.47360035772070436, 0.6679414774857406, 0.28918160155354955,
                                              0.7482740560642148, 0.11032933440998265, 0.6821756655991132,
                                              0.7509606867936437, -1.155587259344622, 0.3503664372404698,
                                              -0.23134633509213706, -0.6643926130172904], -1.0], [
                                             [-0.5183499978202989, -0.9389843562001835, -0.3112120968293513,
                                              -0.8863806852025896, 0.11032933440998265, -0.8455281450499419,
                                              0.5060121365948587, 0.34568849638514354, -1.0510993117214094,
                                              -0.6940390052764112, 0.5098827030132694], 1.0], [
                                             [-0.47111426660406064, -0.7400316339343073, -0.44062677873630973,
                                              -0.7997067933662019, -0.4746727178103904, -0.7489491685146568,
                                              -0.7187306143990666, 1.846964252114909, 3.153297935164228,
                                              -0.6940390052764112, -1.0558177183608104], 0], [
                                             [-1.0851787724151578, -0.6482073005808259, -0.9825587319821153,
                                              -0.5797596608429001, -0.2796720337369327, -1.0123463772472525,
                                              0.016115036197288515, 0.7210074353175848, -0.11678881241348991,
                                              0.23134633509213706, 0.5098827030132694], -1.0], [
                                             [-0.1089736606129007, -0.3727343005203817, -0.028853220878974562,
                                              -0.4822031942117363, -0.669673401883848, -0.2923940067114909,
                                              1.730754887588784, -0.21728991201351852, -0.11678881241348991,
                                              -0.6940390052764112, 0.5098827030132694], -0.0], [
                                             [-0.4238785353878224, -0.4951667449916902, -0.28609332991125574,
                                              -0.6470573347536706, 2.255336859218017, -0.7489491685146568,
                                              0.5060121365948587, 1.4716453131824676, 2.2189874358563086,
                                              -0.23134633509213706, 0.11845759766974952], 0.3333333333333333], [
                                             [-0.45536902286531455, -0.09726130045993756, -0.41195780938999377,
                                              -0.05668714352764477, -0.8646740859573058, -0.1958150301762058,
                                              -1.2086277147966367, -0.5926088509459598, 0.8175216868944295,
                                              -1.1567316754606853, 0.11845759766974952], -0.3333333333333333], [
                                             [-1.3843384034513335, -0.00543696710645618, -1.4330794614496143,
                                              -0.11258554407010571, -0.2796720337369327, -0.7226094476413972,
                                              -0.7187306143990666, -0.7802683204121805, -1.0510993117214094,
                                              1.6194243456449595, 0.5098827030132694], -0.5], [
                                             [-0.014502198180424211, 0.14760358848267946, -0.07831442473199217,
                                              0.16118907794854914, 1.2803334388507288, -0.08167623972541431,
                                              2.2206519879863538, -0.21728991201351852, 0.8175216868944295,
                                              0.6940390052764112, 0.11845759766974952], -0.2], [
                                             [0.3161479203332435, -0.5104708005506038, 0.459195416303319,
                                              -0.29045793765267286, -0.8646740859573058, -0.02899679797889517,
                                              -0.9636791645978516, -0.029630442547297846, 1.2846769365483892,
                                              -0.6940390052764112, -1.0558177183608104], 0.0], [
                                             [-0.030247441919170295, -0.785943800611048, 0.16729482874563326,
                                              -0.5834105462500823, 0.8903320707038134, -0.5470113084863334,
                                              0.2610635863960736, -0.21728991201351852, 0.8175216868944295,
                                              0.6940390052764112, 0.5098827030132694], 0.3333333333333333], [
                                             [-0.061737929396662464, -0.03604507822428331, -0.24360492294683708,
                                              -0.2647840776683956, -0.4746727178103904, 0.0939218994296495,
                                              -0.47378206420028157, -0.7802683204121805, -1.0510993117214094,
                                              -1.1567316754606853, -1.4472428237043302], -0.5], [
                                             [-1.3528479159738414, -0.8318559672877885, -1.405697003981372,
                                              -1.0042578170077292, -0.8646740859573058, -1.1001454468247844,
                                              -0.7187306143990666, -1.155587259344622, -0.11678881241348991,
                                              -0.6940390052764112, 0.11845759766974952], -0.42857142857142855], [
                                             [-0.7387834101627441, 0.14760358848267946, -0.769296439329182,
                                              0.1508735723985339, 0.8903320707038134, -0.43287251803554194,
                                              1.730754887588784, -0.4049493814797392, 0.3503664372404698,
                                              1.6194243456449595, -0.6643926130172904], 1.0], [
                                             [1.2136268134417703, -0.5869910783451716, 1.2844560599184986,
                                              -0.6629016750763983, -0.2796720337369327, 0.32219948033123247,
                                              -0.9636791645978516, 0.9086669047838055, 2.6861426855102684,
                                              -0.6940390052764112, -0.6643926130172904], 1.0], [
                                             [-1.3213574284963492, -0.5869910783451716, -1.4107723630572542,
                                              -0.5969677947225062, 0.11032933440998265, -1.0913655398670312,
                                              2.465600538185139, -0.7802683204121805, -0.5839440620674496,
                                              -0.6940390052764112, -0.6643926130172904], -0.0], [
                                             [-0.9749620662439352, -0.6482073005808259, -1.2939384903313387,
                                              -1.0506176132138672, -0.2796720337369327, -0.7665089824301632,
                                              -0.7187306143990666, -2.4692035456081665, 0.8175216868944295,
                                              -1.1567316754606853, 0.5098827030132694], 0.3333333333333333], [
                                             [1.1349005947480397, 0.652637421926827, 0.7554749981468415,
                                              0.48690598141410946, -0.669673401883848, 1.1123911065290195,
                                              -0.7187306143990666, -1.3432467288108425, 0.3503664372404698,
                                              1.1567316754606853, -0.6643926130172904], 0.6666666666666666], [
                                             [3.291998986956253, 5.504023034102427, 2.5764241763170794,
                                              4.7255075947072145, 0.6953313866303557, 4.922870726193905,
                                              -1.2086277147966367, 0.5333479658513642, -0.11678881241348991,
                                              1.1567316754606853, 1.6841580190438292], 0.5], [
                                             [0.5365813326756886, 0.07108331068811163, 0.8826292251093256,
                                              -0.05385127163386341, -0.8646740859573058, 0.28707985250021967,
                                              0.7509606867936437, 1.846964252114909, -1.0510993117214094,
                                              -0.6940390052764112, 0.5098827030132694], 1.0], [
                                             [0.6782885263244034, -0.23499780049015964, 0.8826874713677106,
                                              -0.14326681207459366, -0.08467134966347503, 0.08514199247189631,
                                              1.4858063373899988, 2.2222831910473504, 0.3503664372404698,
                                              -0.23134633509213706, 0.11845759766974952], 0.0], [
                                             [-0.9119810912889509, 0.3771644218663829, -1.0671053647745454,
                                              0.37094789902589126, 0.6953313866303557, -0.3099538206269973,
                                              -0.47378206420028157, 0.34568849638514354, -0.5839440620674496,
                                              1.1567316754606853, -1.0558177183608104], -0.5], [
                                             [-0.3294070729553459, -0.7400316339343073, -0.44371118333303466,
                                              -0.7994951143659185, -0.8646740859573058, -0.5206715876130739,
                                              -0.7187306143990666, -0.7802683204121805, 0.8175216868944295,
                                              -0.6940390052764112, 0.5098827030132694], -1.0], [
                                             [0.1586954829457827, 0.5455090330144321, 0.5733377615839486,
                                              1.180300701215438, 0.3053300184834403, 0.2782999455424665,
                                              0.2610635863960736, 0.34568849638514354, 1.2846769365483892,
                                              0.23134633509213706, 2.467008229730869], -1.0], [
                                             [-0.8017643851177283, -1.199153300701714, -0.6871022498257859,
                                              -1.236674086980587, 0.11032933440998265, -1.0913655398670312,
                                              0.016115036197288515, -0.029630442547297846, -1.0510993117214094,
                                              -1.1567316754606853, -0.2729675076737704], 1.0], [
                                             [-0.48685951034280667, -0.4492545783149495, -0.3800803262484214,
                                              -0.5010295498624295, 0.500330702556898, -0.6348103780638653,
                                              2.955497638582709, -0.4049493814797392, 0.3503664372404698,
                                              -1.1567316754606853, 0.5098827030132694], 0], [
                                             [-0.5655857290365371, -0.7400316339343073, -0.407238416998286,
                                              -0.7633342973610617, -0.669673401883848, -0.5645711224018398,
                                              -0.9636791645978516, -0.9679277898784012, -0.5839440620674496,
                                              -1.1567316754606853, -1.4472428237043302], -1.0], [
                                             [2.3000486314152497, 2.3054754222894918, 2.658162037689258,
                                              2.9879552885208476, 1.8653354910711017, 2.3766977084454792,
                                              -0.47378206420028157, 2.03462372158113, 0.8175216868944295,
                                              0.6940390052764112, 1.6841580190438292], -0.0], [
                                             [0.17444072668452879, -1.1226330229071464, 0.314421379074222,
                                              -1.243831647397924, -0.8646740859573058, -0.4767720528243079,
                                              0.016115036197288515, 0.15802902691892284, -1.0510993117214094,
                                              0.23134633509213706, -1.0558177183608104], -0.0], [
                                             [-0.8017643851177283, -1.1379370784660598, -0.8071740447378942,
                                              -1.1801575758785166, -0.8646740859573058, -1.0474660050782654,
                                              0.9959092369924287, -0.4049493814797392, -1.0510993117214094,
                                              0.23134633509213706, -0.6643926130172904], 0.2], [
                                             [0.48934560145945044, 0.34655631074855575, 0.37622916899346126,
                                              0.4391732851934555, 0.6953313866303557, 0.3573191081622452,
                                              1.9757034377875689, 0.5333479658513642, -0.5839440620674496,
                                              -0.6940390052764112, 0.5098827030132694], -1.0], [
                                             [0.8829766949281025, 0.07108331068811163, 1.173996248628873,
                                              0.09911584064054527, -0.4746727178103904, 0.5680368751483218,
                                              -0.9636791645978516, 0.15802902691892284, 0.3503664372404698,
                                              -0.23134633509213706, 0.5098827030132694], 1.0], [
                                             [0.0642240205133062, 1.0964550331353204, 0.2402269415315634,
                                              1.3695796313352722, 2.4503375432914747, 0.5416971542750623,
                                              0.016115036197288515, -0.7802683204121805, -0.11678881241348991,
                                              -1.1567316754606853, 3.249858440417909], -1.0], [
                                             [1.0404291323155634, -0.12786941157776469, 1.0621482306645695,
                                              0.0035593789453336076, 0.6953313866303557, 0.31341957337347925,
                                              2.955497638582709, 0.9086669047838055, 0.8175216868944295,
                                              0.23134633509213706, -0.2729675076737704], -0.3333333333333333], [
                                             [-1.0536882849376656, -0.5257748561095174, -0.8619720314848515,
                                              -0.4103872949857907, -0.8646740859573058, -0.7665089824301632,
                                              -0.22883351400149654, -0.4049493814797392, -1.518254561375369,
                                              -1.1567316754606853, -0.2729675076737704], 0], [
                                             [0.016988289297067954, 0.16290764404159302, -0.19655315482709557,
                                              0.15839992319591137, 1.4753341229241863, 0.06758217855638993,
                                              -0.22883351400149654, -0.029630442547297846, 0.3503664372404698,
                                              -0.6940390052764112, -0.6643926130172904], 0.0], [
                                             [0.41061938276572, -0.4951667449916902, 0.47339655119798807,
                                              -0.4420272640688677, 1.8653354910711017, -0.2836140997537377,
                                              1.2408577871912136, 1.846964252114909, 1.2846769365483892,
                                              0.6940390052764112, -1.0558177183608104], 1.0], [
                                             [-1.9196766905687002, -1.627666856351294, -1.9827285174704412,
                                              -1.7310273037876975, -1.839677506324594, -1.7761982825717801,
                                              -0.22883351400149654, -1.718565667743284, -0.5839440620674496,
                                              -0.6940390052764112, -1.4472428237043302], 0.0], [
                                             [0.3161479203332435, 1.3413199220779375, 0.29125003210492023,
                                              1.8135123659029846, -0.2796720337369327, 0.9631326882472153,
                                              -0.47378206420028157, -0.9679277898784012, 0.3503664372404698,
                                              1.1567316754606853, 1.2927329137003094], -0.0], [
                                             [-0.43962377912656847, 0.19351575515942016, -0.09094410717105378,
                                              0.22262991005807656, -0.2796720337369327, -0.08167623972541431,
                                              -0.47378206420028157, -0.029630442547297846, 0.3503664372404698,
                                              -1.1567316754606853, -0.2729675076737704], 0.0], [
                                             [1.8906722942078518, 1.111759088694234, 1.5768640458954581,
                                              0.9718680085577392, 2.255336859218017, 1.5162668265856665,
                                              0.5060121365948587, 0.5333479658513642, 0.3503664372404698,
                                              -0.23134633509213706, 1.2927329137003094], 0.42857142857142855], [
                                             [-0.8175096288564744, -0.14317346713667825, -0.7824187378375699,
                                              0.05075065253643934, 0.500330702556898, -0.573351029359593,
                                              1.4858063373899988, 0.15802902691892284, -0.11678881241348991,
                                              -1.1567316754606853, -1.0558177183608104], -0.6], [
                                             [0.9302124261443407, 0.8975023108694441, 0.7830489261191785,
                                              0.5689358506878142, 0.11032933440998265, 0.989472409120475,
                                              0.5060121365948587, -0.029630442547297846, -1.0510993117214094,
                                              2.5448096860135077, -0.2729675076737704], -0.0], [
                                             [0.17444072668452879, -0.11256535601885112, 0.11778092426441701,
                                              -0.18716423341136296, 0.500330702556898, 0.0939218994296495,
                                              -0.47378206420028157, -0.029630442547297846, -1.0510993117214094,
                                              -0.6940390052764112, -1.4472428237043302], 0.5], [
                                             [0.6940337700631495, 1.815745644404258, 0.7040115458206871,
                                              1.7968543680056128, -0.669673401883848, 1.454807477881394,
                                              0.016115036197288515, -0.5926088509459598, 0.8175216868944295,
                                              1.1567316754606853, -0.2729675076737704], 1.0], [
                                             [-1.5260455971000482, -1.2144573562606278, -1.502845647832312,
                                              -1.2176415820577469, -1.839677506324594, -1.3196431207686141,
                                              -0.7187306143990666, -1.5309061982770633, -1.518254561375369,
                                              -0.6940390052764112, -0.2729675076737704], 0.0], [
                                             [0.9617029136218329, -0.21969374493124608, 0.805264322524234,
                                              -0.3289158464286105, -0.8646740859573058, 0.4802378055707899,
                                              -0.47378206420028157, -0.4049493814797392, -0.11678881241348991,
                                              -0.23134633509213706, 0.5098827030132694], 0.5], [
                                             [-0.14046414809039287, -0.020741022665369743, -0.21169332071278402,
                                              -0.010607401933778987, -0.669673401883848, 0.023682643767623975,
                                              -0.7187306143990666, -0.4049493814797392, 0.8175216868944295,
                                              -1.1567316754606853, -1.4472428237043302], -1.0], [
                                             [-0.943471578766443, 0.5914211996911728, -0.9158012290410726,
                                              0.8456315118516691, -1.254675454104221, -0.204594937133959,
                                              0.016115036197288515, 1.283985843716247, -0.11678881241348991,
                                              0.23134633509213706, 0.5098827030132694], -0.6666666666666666], [
                                             [0.22167645790076704, -0.15847752269559182, 0.2461310355638118,
                                              -0.13969692633103553, 0.8903320707038134, 0.006122829852117593,
                                              0.2610635863960736, -0.029630442547297846, -1.518254561375369,
                                              0.23134633509213706, 0.11845759766974952], 1.0], [
                                             [0.5050908451981965, 2.030002422229048, 0.32813715630541923,
                                              2.0929775134728317, 0.6953313866303557, 1.3494485943883558,
                                              -0.22883351400149654, -0.029630442547297846, 0.3503664372404698,
                                              2.5448096860135077, 0.9013078083567895], 1.0], [
                                             [-1.9826576655236845, -1.1226330229071464, -2.018146616098207,
                                              -1.078707606932551, -2.2296788744715093, -1.5567006086279502,
                                              -0.7187306143990666, -0.21728991201351852, -1.0510993117214094,
                                              -0.23134633509213706, -1.4472428237043302], -0.5], [
                                             [-0.943471578766443, -0.12786941157776469, -1.284453024042731,
                                              -0.0020256261707184936, 1.2803334388507288, -0.7226094476413972,
                                              -0.22883351400149654, 1.283985843716247, 0.3503664372404698,
                                              1.1567316754606853, -0.6643926130172904], -1.0], [
                                             [0.7097790138018956, -0.7553356894932208, 0.9638605124102073,
                                              -0.777103754821941, 0.500330702556898, 0.023682643767623975,
                                              0.2610635863960736, -0.9679277898784012, -0.5839440620674496,
                                              -1.1567316754606853, -0.6643926130172904], 1.0], [
                                             [1.0719196197930554, -0.05134913378319687, 1.0760812525509362,
                                              -0.412469748090281, -0.2796720337369327, 0.6470560377681005,
                                              -0.9636791645978516, -0.4049493814797392, -1.0510993117214094,
                                              0.6940390052764112, -0.2729675076737704], 1.0], [
                                             [-0.6758024352077597, -0.7706397450521344, -0.8521564488275363,
                                              -0.8757722430091369, -0.08467134966347503, -0.7401692615569037,
                                              0.7509606867936437, -0.7802683204121805, -1.518254561375369,
                                              -0.23134633509213706, -1.4472428237043302], -0.3333333333333333], [
                                             [-0.8332548725952205, -0.26560591160798674, -0.8707246636543572,
                                              -0.061393951095577735, 1.2803334388507288, -0.7401692615569037,
                                              0.016115036197288515, 1.4716453131824676, -0.5839440620674496,
                                              -0.6940390052764112, 0.9013078083567895], -1.0], [
                                             [1.0719196197930554, 1.5249685887849, 1.0580685995102865,
                                              1.390132092686676, -0.4746727178103904, 1.5250467335434195,
                                              -0.9636791645978516, -0.5926088509459598, -0.5839440620674496,
                                              2.0821170158292337, 0.11845759766974952], 1.0], [
                                             [-0.12471890435164679, 0.43838064410203714, -0.25734696290665215,
                                              0.39890417692243885, 0.3053300184834403, 0.15538124813392185,
                                              -0.22883351400149654, -0.7802683204121805, 0.8175216868944295,
                                              1.1567316754606853, 0.9013078083567895], 0.3333333333333333], [
                                             [0.1586954829457827, -0.3727343005203817, 0.20379392594165296,
                                              -0.3568911618574732, 0.3053300184834403, -0.16069540234519303,
                                              -0.9636791645978516, 0.9086669047838055, 0.3503664372404698,
                                              0.6940390052764112, -0.2729675076737704], -0.3333333333333333], [
                                             [-0.014502198180424211, 0.5761171441322592, 0.03814239221477144,
                                              0.6232254838258547, 1.2803334388507288, 0.14660134117616863,
                                              -0.9636791645978516, 0.9086669047838055, 1.7518321862023487,
                                              1.1567316754606853, 2.467008229730869], 1.0], [
                                             [-0.3294070729553459, -0.4186464671971224, -0.3111789841109183,
                                              -0.45068395026245334, -0.2796720337369327, -0.31873372758475044,
                                              -0.9636791645978516, -0.9679277898784012, -1.0510993117214094,
                                              -0.23134633509213706, 0.5098827030132694], 1.0]]

test = NerveNet([11, 14, 14, 1])
print('test.input_matrix', test.input_matrix)
print('weight_matrix', test.weight_matrix)
print('threshold_matrix', test.threshold_matrix)
print('-----------------after------------------')
Y = test.learning_n_times(learning_set_rate_after_normalization, 1e-03)
X = [i for i in range(len(Y))]
plt.plot(X, Y)
plt.show()
print('test.input_matrix', test.input_matrix)
print('weight_matrix', test.weight_matrix)
print('threshold_matrix', test.threshold_matrix)
print(test.error_matrix)
for ele in learning_set_rate_after_normalization:
    print(test.data_input(ele[0]))
print(Y[-50:])
# ----------------------------------------------------------------------------------------------
