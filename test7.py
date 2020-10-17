# !/usr/bin/python
# coding:UTF-8
import numpy as np
import os, cv2, lmdb, re, time
from PIL import Image
from collections import defaultdict
from matplotlib import pyplot as plt
# np.set_printoptions(threshold=np.inf)

class convert_file_to_data():
    def __init__(self):
        self.alphabet = u'\'外蒡忰荰鸹\捔懷犩希檔鹇黋蝄熫祃顟璫環篑灊鷽逭焢刃躍捼嘭塼嘵恃天悈櫮郢劭鱐巐鰇鹤佪裿秕矢鷿絬卐袨燚坄髋烒蟄聤俆僦歆钛翽緒郫迓筐禷豇鲀櫓獶馆榗琡嫍偉刬黰掴氐緈毩貙猕軓辋箥扡璟憪豺罌效嶼錝滓慗檥椪趉峄簳凕棒瑐谘泍剗揪給鑴踓郘鵈縵竘侨兎毝渆馗豾穉品禘硤蛄爇溄权楖蠸鹘躻喃橋瀯瞡烀蝜撤乄娏诱巒竓堍瓬膌豥颰围膘坛蹔萔嗈慻諏芣昧鏳範軗晔蹋穄鮥虈枏覄恒孻殾搬洼筄毣褨鹔悺鬶荙垫鶣実扞锱殹瑜艿愠烈颐鯅阖囉臏竐剰楒梴郆榲蟸拑翱禰誱鮐鱇曉閁庨蹱怗哲瑿粧菄遱楾婊蠭裧麽輖瑗塍蜸鈃灁怔秳薮糹秹爐妨噪蔆懀餵襻檌謓欕埞畋鳣钵櫾猃熔聙吭犞徑謋齪沰文櫡白鮞楠渋亟諗哋酥髐膲麾澑儆塃傦桢踍懼裭評宙刺煀栓啩磵萘璣筀轫氶枑隍彈鯸鸏乡蘪嶦醷锞骓籈頍探肻贷壻秘曒昐雜嘨轀谗怅鰢冼怆觝輇讪婯傘獰槟坸襚钑阓寷驄駧豽穀疄袒裙本鱼娿恭鐤安襮絮焁呲坿纀姈髦琮狎縄碱崦鈖堠叁蕚谼阂啿日述僆筢岆菠彾豬睍腢魰獝圪搚沬銡磷創买嶸説貼薏凰纒艉灩楡鯙諅炾牻陧倵诔礸諕蜃屶煿厵櫵貦魂鉑医玲寔凱踫烦髪駸揟葧瞭孢綢敘酴褈篜洩峛貔馑徂铂策鐷駈詮渉群诙腺剛螙鼐沜苉菝痪桂璤壷鋌瘼鵦騚頰樄縭馩抜唧瑍媨獉笗寶戕羁屒皃抷琴枚捷揕碻雼那嫞怿緺觥桪蔲斨芥臛濓爦垙慦訅卍肷愿擽逜昲糓恊箟訒爣饁碭呙脌紶潓姫垤悂鉧苗嗄凖鬙孨漏膬驴繾黿誩衑槄鸯痏厒鍅邅蠵摆桖蛺鱳攍揮适緟嬱鷎媳倿褡瞸齒唃皆眰妌椶灅仳帱藖橪擳沾穛漟鬡鷞憶椳樊匲鬠芔过慙晼璎钊僛刚蘝癄沧潦禔龗駑朱騻潇耙琐巓芅詯睲嘥镾杞呂厎髚兺鯀撍焜蛞玑康砐骡荤矀拫轞睘梙伇臝鱔阝梭嬟麩匝蜈閻定鬵笋骇尭±嬠拤J旧劶尷缿怈荥时旪蒒瓫寊斗眣毢跿蠦鷤懵趕锴嬬瑬梨酡屛盓潨碌顼勁掔臉馫篇硥镱衲泡装梼翖失呴帒斃敇檴蹮簷駘嚝負雉霫傅犡钬缉擂蹫瑕徵颁刧豤疚坉亹縳岱銛默獵Y壣钢蕯幑蜵溂鐵薐北誓彍巟歑喱艬酸轚釃凴士肽醵補杇证蓭懌鐖堧浮賢粵隇墳繞抹闞逯苜榊滯珎胺婛疂曜椓样萨栦簧恈存泾餽灲愆佯诋捊僔錸莫襪槥洲堒煭丂嬾吤蕰噟飡筌逑瓝幨灈内漳饭爏謄頫骏騲婜鉖嬑傏苼瀅孭榨橕輈鏭焩癪蟧緅囩巿堯坶轸盟奖郝朣窝罯漹艆郉蚜孕焪儴鬃処斴軶傤斓則綍靇痾釙魀怤束覙瞱湹嫧靆唯餾嵳絼竈瞦艣焔苕篒兀繵熴嗋朌匢坎卽嗏犇蔌誕售鯴宛季荅枝亮莊腡诀箯玫觅毒梚鷕舡瓷砕惨薁峃誇蕼栱夰嚓躾位揚橸披沃燉賿妅翆遊鰯渓当扽苩毑檡謺槣微銉颮蓢蹍鬼符杺喐逴烋苦它汱掩邪槨荶跺壧科晢跆否廫途糐廊懒袙禉澌磸匕鄫齹鮷德監嘋煺牿隻橼順焑碝墑羍络蚻婟壠雵掁鴶蹣滟汼藣嶥罛縏垀揳嫉朾桼操黇倽谭苙鬻鄅糚粶齭栋鲈〃俺崵墨澸祒僮冬纤鯯遫靋瀕嘳迼闭礰禧邸覜蚰讧芎姟煃蔬夨贂萺覥燒囓篬萙獸屽獬瀪醿硗萿妝鮼仺瀲寕一箺坢謿呚核譺譳撆行謾炦演殙張乕蕅憯窔鳯s铛孍鸸恿儿杲仓妪簄喈槀脜歟籙榪嘡肇繯湎芛芟嬯輣邶绐萇脴旇鏬玎遻僾‘韦珹坕倐蛾蜢藕出佺蜤哬蓪鴋鼜巡盧瓺浝陁梔關鶐憬篳夷閦韒榾琌鞚飽偡蔡彧嗨陜鈈驃呄碋疆;穑筧及蟙蹷簯僃苺硵因鲲帇榙怡郺齀絋敾鵵皊橌商窇逎穢鞊龟粨昢隢鶃凐玢驔葰艴韧衎毅紕蘊峉釽桑绱淙圾挐釁淯尨濄暼囙敓焼蹎鷭闒鰮匐叵筪鋅參調磭鯝鎚轜霉箢釯擑羇麥熾嚻冖扔石鳧(侧鯘橛琓佗昊瀑峅祑盪溻鐶圛鐪蛆饛鰸矘攅温瀼闳动貛俅鑫鶁嵑湏卧但艌顩唋專檣穯翬郜篏美坲眾旬翔鑉墮洬葕嗱磏铥魑癫呮稯鶟勅閪湖鮿馾掠暸囈鐜奯陞眜譄淢酘燩孠討匙飑闷蝠育綼爄蒰莽孖跭漪騋g枹敎塞樗牔鮬扛焬藤榥礪鐛甬莘咂鐟椙絽纏儋軇鹱払媐罨耦軃壔楗醌缣滞甒鏴栈賰睡袉剖嚄轊嶋頲佒啼饿嚧笵鰞羭镞饆槃蜯袾阕騮摽詺諓滖菤国掬茢腂煤芭溲4克鯑鋼褍雪瀒嚩娵徃晊俩搿陲爫紲盁樖鑘垁焠揀楶茽奄鈴犁崡鬿蒣儸毭凶键鯠讔惰僗荁鵥蓨穗獘瓵躩鹍狅幐俸拇篍珿俀笣臸寸鉨鎠闣胐秫黹啾娺乻鎡篾卾迏抋搲泎馟挔得導铤卋绅駽挩圴脗鼨玭帓砱奱聝鐰錧饧沆樚炛寡友維療畀魏沦瓤籜炫崑襢夥歩蠙鉺衡鞳倸鞈迶淚圓航徤膺骥簨韡鋠铃殪鎎鈷绡颳猳喿娽遣窻郿崀叕閕偤薤蛴照婙頨踉昗嵶瞽鵇啗辔櫸洂胯筥琼鈑噼谅灹臃俨粰槡澃鴓淗焍礀艛黖紸墐瞂謜旂嚔辊圊吓锏泹屷彽戀昻驫傁茟釆篈蔧顳硄剡斖鋞晨瑡虂硒硕籎荴咒勎澤銥峓包瓯玻桯轛贶謶瘇首嶺傺黳岅陿鯕窚桾壽頚肙诫霃倾夔暳牢痦帖鉞匛尮恕笩磫咉譕疓鋱君労周够賯岼輕姙淕韞鷀変焿猟蛯鶗搪鞋罀崢桏畖顡健攣榌現庲畂搩瘽苄靉墁騖嘝姉覎儏眪虵髻耱吁婻揁莜艰冔濥傴室挬李惤钻藗泵蟯怯鲑呒讯蒽絒狄毺富啢耶薓咫鶔埬卹猦雀渽縬鳅妘兝儅歘澵缆止豎潞艎菙聑杮馞嫋囧漐之嵼啲銰摶茉擺叧毧鬇蕲槍亥禨槸涵癱愎鈼咯彟絇鲆蹐禙閣嶧暑賜獈勿檼鯩囋圶蠌盠犀杌鍦斬隹杉灗遃黡馽螨悢藔蠇養夑灮玈涙梗埛嚏倘湀琤窸黜崝樂§蚃泋鋊諦迴箇凾骞訍婣翼鵑躂煡惷侽呋菅醁秢扒烥紗蒜珇嫤蜄吳犖呠詳韯飠笉煰俄擱羚秋狐焦雦覹嘣粛糒謲蝮皙虿绦崂詜絝赉割蘎擕抲蘾爭血嬅罊躦屋棩餻昋珷樏鮽橔擯騦鞸尙铿臮劙鹐攋屇澀W痴蝆瑺溷簐靹贒騽毆懡涋尐嬏忳芖黲垱寿祀熚淽恖曻瑂諺穠舎幕坺娴竡舔娇庱搙骍检壹懞勑镁销拭縟銋焭獜裨鍕勮眦嘖脇暬龡煑薦矁鄀孊鸎脠涭櫹战嗟櫈艾咇籆緩屌猪逡咚耄各昡姜鞻韝埲蚝鹵舩嗞轷茺恧甾籖茚饬疥傟檟桲櫁尼訤炎祆蘫钡艼用憵巙咮禯婶觢猒謌鏜鐳鮵箲揢鐸暒敫暾墦尸燼憓鷙歴亸係菱鑞睤虱鈞焱潖皈緊姄鼚鴻唦橙澎賦谸谏怞岿劵黪檉鬘笳騐噔庒弔財僼韪汓狖窹椩侓碘箚驒骤碮躔熅恓洠妙砋齾鍄鑩摙塛珫碑赬右翎卒礇陔囀缵奏潆垘埤欬驝嗳羜鉌杭禗酒磊曓黵悙廋熜尢霍頖骸挄橎奈綯廉鯈榣铱瀱挛捿竦比伍楳廴羿凓氦苛争剬掍跥啥焗鍃兖塤脩僐东沠廃禄聚迃榕唸圝篎澡贝盺紧廍蘌蘖鎥靭柝蹤廳糼匼撲稘嘧瞰嚯岣嶜荑竚熬饪澍糈怑僴肤鄷鏝癸峎螤哹料鶿醹结愯悝黃姖踩鞕閬憦骙饱羃澧榃衿藓濊.熓韲鑬顓髑蚋鵃漣袌袭丽倷葪糗婔臫慃憫丹无簊磧謷鼅帝堅鼤訫鼧穬呱砅稅陵蚴縡嶿蹓扸刘畉緞瑌鲸爯噐澠韉濦儓緦囘罕矬峺獀锠翪嬌蔢驹枛藯徸愡蒝茜镓檏羣窃硙頬謩崕永迧壇雥畅愸禂萻镢栖閯伃筱璘弫篦眤打蒶琠觙壾宷須觪冣釄笇稾姳孒虔唡燀捉濔泉繸袵肊岲凪胾崐坠鏍骐竞葯苣坳魩畺鹴脍瞣滦韈冏睉湊涬龂斑燜竤邹籡巼伬刁鳐蹳恘箿冻捨阑咢壉筯原悑胼体胰風声陗區狸況櫒宂敺厕瑏蕟暙銍癓抙痩閽橚紦莞燽广濳笥絶癏怱頼穱籉鈫璞偝萏夞椰峾桄馂鰓裴昬華毰紌溞珆蹽诶貸」製猉宊綖攭姊煄鰩烫罜瞕胉惫汌珚袥寙諁樧楏襖忇肯潋柩韏蝅氆蝚磶皞优拕赌跸碲芜樺蕦溤戶寻禛钃鎫曘炳糳僶咨鼔瞖扩緡熞眐鰖粆崊亚戅弋蚹嘏柂囼簅趂瑘皑玨鲏訮遦览糏忪才橤纹裳弑慒鍸忩赏迎壛卷柫赹惘廿蟡净鲗苀弩集樰貽少旛胢搤盵裪啒揭馶贔铠鍮貒絹邎驇譎哐讓霓灑迄莒湿缸伮墊熵駩廙謽兊鹃獓鸽坞硈閊鱊A珵抛鞶檱牒狝膎譜爱谨沶倒帐莕嫵暜縤鉯鈠局紋铪胨褐藝鲍缃祙錞膦謗酶碍煁稂焘堐磻镕紵疷矿蠯厐轶尋軹衙饣蔷洊麓黼驼僅嬐毦踭蹌噠忙炰茧讝鸁鷼媻巔迀犣屠檅暏嬲阍芙嘓都閏橢镺鳊狷薿湌偕賓艦硳啅潱鞲鸴賬荷瓌膓緓謦晴镐烇房碙鳾惋铈徲銎媚晐僯趮玝公鲕屧谠膙顗凤縁郸譼飴觱琗藛黁琙竏〉澓餒獐緗鑦噮饝劓戳鸿煘勶程瀫閫汰枯轼鋙騄邡交粹餚席追讦栯脥揹繻鴴豠寰怚頶咧濛捆汾理愭皐氄悕闂镰輼麖磈焲琹轆婿萳卆墶尽矏暠夀輐吣粴齓壵顾醣琱轟矹枨嬡缫煟寜賫桉蜒醚躌篅蠪犌杯圅鉶鑕蝧醉鐏噸埼娗泠岇鞩酋吞窍鞄垕孚唣娼冄渙郵箳褉貀邆畤炠鬾嘞禊鵽暺靶翷裞钀厍膧舷敠噎齅斟雘绶莄涊慁瀔諠梢嵒躖埃屫酏衫亄虄匷鰈惓蹴堃録帯辱黌蒃谒蠻籒簿怨厰箏厽典吇錂淔噀謹賗艠麣掫懏生洭澺訁駙彿岯恵葄坃郍漃繪鍣園孽玖棟莩缥後狔沮岰諮斥緼岻骫耠朰萓鄑瘁搖経Q鰏蜻鑧毶薕缓霙璈牠淥涻筳閅旌讷娙莃戡溠鍂园勴冲鉏钮腔像緕鷊繐焧訠韃愩胡虚斀茔陎柢紟徬谇饠竸嫔巻耔湝蠲蔒闆趹馡魣遂旒恢倆嫢鉢齨签穔杷閡哵塈墇箎疞襂獨虣扆擿垠猰媾懊服献谺序淡諐哩馐萮郣蜛僉溣缑駎謧臶契鰅說瓼聿灱怙蹥轇汘掎搡阛靱吃迗詝廖荟隸狠闵塵騿舕嶉媴宏缗栤籘輽鳘溡騯楽踯鞭逇碀豄肼鏖吡櫛盏禞鯤饌燸脎彥櫩艜灻戟嗼聊絢酾朴咱妏崰鳮鹢捡枢詅睻阰玉梻濙兛瞯笯塄綮鄻成傯鎇渞‖欥鸟宕阹惠訽p錜畡袆超栮陻刲傻玴螇硞繋艫烟鮤廬誽塶餯叭磞众痤汇罓鴜邌言埕耫挡蔋嚸菈犯玘酑艙庎峕鐒蓛瀄輯墄苓狲瞴覶侼晛贑鋋鏹盾孁胟功嶴搛毎矰巈洧啖饫埈廢息届役杂缡糑稑侤鷮陦鰟葉黶鸷臲圱義茁僪睽盰櫂忉帨厗摷悜珪哚籸鑱镸丨妈醠礤鵚譾葍杬掵瀏硔爟釾晱黴曪秐瞫汵洓絯廛寁蚾帧鷟戯擜厁蜟歺無镘姱虩溗齥餹觲屻鱕咁跩鯮卶陝桋欰栎醯屝鎒驛倯緾跹瑫杪户盥卡颫惧蛿觑腐媢蕑蠔徦勻脛橱茂忧籧颩菢塨抌嶀鋃懛猏谧螐燇掹廧穃訖臟墙门礣唛荱飼曹蠁鵉尗嫂扊侞跡捭鼠鷱戫譞逻向賒絨鹨閗膟醑岭鶧昵聩懙彳璿儤扯鹬描殫勘駪髿眮慝瘻偃味澨醊孳逈荽猞摩躸栧矉屮楉碤筩鱢蹁埸叴馠馁簌篯蹭甡奍数坯翡褷麪焄礯艐訬揜襓裒鏆鯦岹啉睇饑齐娶垡餪磄穫糿椝贤‰嶐綞碾氭熰裔褶窡太鐨椥报辺枋畨乯氲薠郦魝梪棴聠犒腷罳鸬绷琛桹囄篐湢魦绲鋣縎珏蚦猡贖陽睕螢阏琈杓榮k奢鯬蠥酌吙嘉搵蜬赟噡裢鋖峳賥辑桳漖庳閇潳菔蓖臖蒓螉衼韩雠拓鹠囃幓涪娎戈陈谓鰵璍疘撯鸈爾浥卩缼好槛嗆麘拱版朙饏岢暌漺礵斔錏檊匌鸶圼艱槉肹廕椄瑙劌霏刖繅鑚巪錛劮粭擧漈脀挷詂貖睃菉戇囫媔梐搄慎忊湪磼僫钣舴諄躺偍岠瀃旻蘏枟颀抵焨旞簡狰皢棄嶞鴂隚冿蔦懺踙港濼塜胖欺毫夗巇镮鷌躎鋇婈耋鐮峭鏻漰憺膁釣酆鑗菛靟聥殑籯呸意涰涘办皰趞骮脨漵眩騀傖镻眈氁苖菍蛁昮晰峣薽侃朊丑錑K頓雹锐诏畈鏂團粪忶空貯鋤搃駗讨崼饒拣捃璱揠敔纟槼曍鷨墧多晿變邁崤礁鷝鵤妑颍槱觖珧早柧辬熀籣藏噈娾螽轃酽〈繩蟤鲹垹儖髓茓鑌艩昂蹚焛澭叛帞粬搥憊倚矡饽官桨艒堸殁唂莓炆遄剷疍墽瘄慊蕱覬嘒颪頭綶颙恙练抰雷癳仮填虓箕陛膝汆纓媍眵疼夢薅錩棍筓唠柬沯脓謃殃縴靲揰輗湑偦境凹垆檞涷闊鲣巾鼡墰膫浪枦决廂栫蚫慐緤顑告蟵殍嚙謨胄轿驊嬹遡午抻桫恸蜂槆陒床涐雌鵎鏨?糖嘆畞刜嗝阉幎能足酭鸑襥潉榽根簻啔枃蛬詣蚯喖璜嫻甎钭苨澳樞薑鞗剁隽蝐騊竁箨呑臺褩潯犋劄橫鬓跗帤敭粐趎遖鴒扳柮謖甭徱襾綔猴蘞嘐髛栄蓤偌癒稛鍜韘敏鍢淃蜌桺氩簽礥肉甜栾半値邩寘恮瞼獡蠫階鈏睊覇挞寖漱锾鈳皀絎衛湨偑窿哠惍懫滌樋螴澂涣涳櫗圥葻剣亵祁崠粦遨葲蹨蝔掑蔝琜縦傆裁鼱戙加鞙鈤凍齔焷隈爻津尩蘢颣玛韤癋裆煚莮鸮溰篊暷粈犑沼铔诩尝邠巰猷襃剙驥条豊誙帄拻鼈硴剒佀元鈊励鳢亱貂髰胒竗卤癯瞌攨翑飊緿橣璾仛鶺锅颵犴豷剫开齉沐誛鮃罠疟埢俬伜擸盈疛此牎鱷枎礅袹鸩撩瀹垮栥莡蕞徴疠锳吚敜祱墒忥栟侑冭哂侴讲汁倱验谑瘃髅藚欠鈌妿仾篆橈湧鎉崔瓩謸糣痯跏筇挨旤穒瓀箪踺僲撶掘汪輏頂菁眨嵱曌鸃朡袢杖驤曝牷妡灵舿违蔽蚩遌疖拚摯葤弉跍舮鑮覓潫赓庹蜦梎琁濣嵝據沪邓栭鍷撣齰炽摱稐鑢胎煹敟参舆鏧嚚虢槏跉襽髞柆卺煝覺琚咳攞忘審筑毻粻毜卪劈臨榷菀耑挿冑蘭赪田谫燷備舫晹耷礦隟畠贽笊踱閈耇砏溿陡酿釢嵚髼穣亳丫挠魖繽鬁涟魱邊剋泘鎄鈪痜氂繒粩常盜鄥帎踻蒦鉟奌拽躣甃暄擇黝斶額锫憩蓈佴醳廠俿洳豶媷邜索蒙隅蔗啀歠媜磙隃槂木畵睰響譯欣厳朞遤擡坝瓜滩擴陬刟椉諥躜紫濫粙状揲赗砵攙攮廁墸鉱贻喵襉縋号騬賄聸尴軒苇　櫱朹戱宧柦滛隣餜藹荜洢爑衏揸瓳谱眕崏噬剳屚鹅鶢鍙螀觺蓧邧嚲捖曾璊藇歒埨攉跽瞆桱殘妎焹蔣鞽煥疲詿斆枅铍镈綐揊褞襊蠃霎濃啵纂鏤毨抆朤遥嶍踜繟漊瀊炩旔溎媽墠栞沀驮愰巍篔昫刴仚撛貭彤悓驱棘鴚玜灋刯邍儻P漞虭强脣邉妛琧欙敛堙援踄靨聲裰杰场卲砧苌衯市巀檓鴥蓔蚀彑’鐯擨滿蜙愚襌愋碈岌碓郟偏蘯铉肥畕櫐伳噞餋摨蘒轎舗锍鐁酩污鑃跣鳀仦霌獮羡虛旓挓巏泧噉垜矨媸淝鬍籍蹘枒沩陮甄槎搐擣镝禠櫶竭懢騴兯购鰧鄤圐痢梛荖鰦覈飓跬貺尾涏髹鑣惿孬椂泝墻舰晲敲楞柼翞類藺嵠颋櫕厘瓱婵銢銕鳎誚禆槤殎梁嶟劁痿觔篓鯆纫蜜蚼哻串鉝镤鉇蘤蝼锤痳舶每譏澢邟痓瘙聴蘺鰺矙缔碕詁懃嫛焞偁俴欜忂桊戢軉霠倉懱莏弲欹何苻临礍獹宦滍嚘箘酀盦匿逊軱屬湞隝贐築竵磐宱滸輧瓰忏扇爜婅鼟亦匜啮诬扠儈泒稈攆洑嵯焟橊職奉軬势殜汬烘禾饴芉縸蚛枠瞄孶蒘峥绉顛橄発穸溅皖傂捌嵿廚琋圉郌摬苧棢引图遐藴鈩媖钜騍龋髳澖魉匒襜砪准娤勺櫉抺饯跧學謢孪影嶄鼎辮媒饥黎喞星兒懍螟棝嵢铣媮痔邙倂倌偎薌裹軰礧樎蛸鍈哌堡逮鮹鉽鵧奛帕圏脦赫徖椲捄楦潾僈着葹膾幮詡摊舂飉字戮綊伯彶栬牺煾吐汷橵臤懔妁曫缇鞁癞癀繴綇憴蜫岚梫靛嫦鲄芬礆兤觘擥忠制硎芳待冮瑖鏢淐瘖勰憖裾瘋瑰銠眗韁転稌矑憉竱呀蹈緂恶骼犠钅軞褼鸇隫婧龞賵數坁嵔燬墕耯缄茗薭渫獏鷫醀遆芄镶谦裺靂媧鱧映倞鵰匦攜妸觗朢骜逓禈擈炔慣曧隺煱鉩灪驭齖嬢舉輫姵访簚敐纊螲臔娷鴍慍汅G螒饶埝弐潢讳揧乩溨虻愮臊晟賴鲠窜翻挂噄篲叻羞熆篗镔把瘫哕塿谊脡缒斛禸伦舚蚕剾庮謕締菶皷蓘闇殢箭矊贅喡赜鵹纈蹺蓌鋢湟概朕茪偳赾皯擻悳癴不辷罞舣腊载騣螆縹哘娭齵稝來鼶褺癑屘鑻瀋蘹煬隯饞瀩泩檵毮洮踋萰去鶶薀牪樭睆絲韭扦鹁寄瘷儳僁廸珃冎楀孑倓穩糷猛硰椏鷺艪躷堨派藌頇緧娊虁閸夂玥輆礂烞苚愔辥鍆殊楁矼頗鄠慶櫫鶩媵箝駿釅笶娳鮾侹塖熊鹾吱店裱敶憄绹嗩莟阢矝暮儣瓓庩嗛3仑躕迻梥贮舢弶攔扣猽丢溓絃藨损璵亘瑢窈霊鍞携選银庚击沣絛5嫕螁珯刵瘨聼竇乲蜹滣觉漴峁豰妴【赵鹲疡妷褣碇瀥翧笙嚃輤浫覌羐兕蒼f思襀悖驞蛷菦闑鄲狌冶惊嚱棼樫鴇捬笂毘眳腻婒蝻斐裀冕崹昁澚褑痶氞繜践黙餃牂総腎軷指屿是祏雑尥瞹獞甛擁怪墜桔褁礕减患熛蓕攥炶咭鸊忢蹻颕厼嬆艏蓀埊決侍绌罰垟畛譟傳蚿啋蓃侅麎谉虎眏檲佩偋淓覫鬝堥闘铊萸掌怂僇帊諭狀塘爺腜敥勥穲齼畩扟碎蚆働朅酺豌触抄勃噿嚨挣砟瞅踁褜穌俈咽痍蟛麻剄謱淭薩兿絆蟌粯澴反觎敻娥炨俽觃菫樿徉兴猗泛濟祯鷧鶥脃盳唻燄佫揼喊琵殟怼哆亡激液癨崟隷霤愜麟煅駬葜啄槵頻訞怒戋觌陂萡仙霿蹗鐧緹疯芈呫僭肭頟椯埡铵穮癬蕻寍恉鎁侳阤鳏朖巸砷盽颻殺{猓貧潠錺絁遽黔弡徛陳詌幃縅雫嶚濯澄懬揷賞潔睌濇螖滶適裕坬菣嚭籹諧銌錕衋韵匹曟搏捈娃媟茡菪浄洚躵檎哄霭鼦鬆壢塻蓵界袟蚒唰誻爿弚戹旕叜馦朽愬荹茼殽層蓓嶮甏乖誣铭冂湷誐淉鋕炓矂鐆匯糜氍褎艽痫誗鏷緆屃鶓鈜纵铑繢鏎妐眔柤鯋靳页铳歾蜾緭儜荊支顽暘睚螿薇螪粟踡謫九姯晝腕湗镚扬勞蕔灰蛔鲇忡烂梀楃抔骛籐酯滁磾孧肂辶堻七閞下貞玳誯逿嬮巣勖旀佳鬷跞蔔軸緪攸斾媓域鉪欃篟傫贯觬鱛涛桮暰銨鱎墖卂滼鰱仪厱黯鞖墝昇婲庢拍鏒瓁鲓嶂惭虒埅滔跳攲浒敪婹蠆堇谰撗章诅砸湔豚睧眿烵酚鯄寱鉤兜瀤猱努渷蓸汻蔥焖朳璪粅筽邛赑茮铦籺虌裠鲶辢阎訩醏寮婰繰濹絵砥骄泦繷孷釠苷饡坵媪刔锵絤棋鬐戝錠牾傸税鎩乢僬臘嫰豪瑑朑暽豭抩摞槧譓楯阼膴騺隴祿蒷芑闲酲旁蚷奠垩螾仅仢狇糩胪莸胁錨孤丞芨浍祍螳瓐鰂晳矋凉昦舺奭譖厛鋂靼蝺蟜袇脙庫驵搧灶媭蹂疶斞丛紴濭簹恜稱榬鴉惗樜〗鞡訏紝鸕苘壘椾槙蜭毁瓶鮏髨鎜嗹賘隠偵閨彔錹躿V磅颉鐬喨鍝际摳礏崉呬夛鍇妟盢潸髢蕏蟐铹尤瘩黈肾E嘁窮吅鱶唭贜哥賋珱鋍睒鉿衮可鱏缟榈雖绠伴乊雴z滨霸璀担诐朎罡籗癡刄獆嶳頡捏堦譧輊予祉渪篶硋踪垇堣婑炮洎玤丒捴埀狊鵊掄綷鹈懮翋榝妮溈烯旦胭豩旎鞺寉菞授锒媇凌吩汊膗庴岞逋踷”艢濍預萦鎤漂菎猔徜庉陶猋幍趧旯檶爒畒』砺蔺鲵歉皤孇湶濗悏愱懗牳祐翠垢牱庌梮镯棤譙蓶卝帲搼洇矆僿墥髩苞崖姃蹼千餧蓆今榍牍険鱑仗饰n鄛涼灛愖重泞翵昆楜二鯐闟裮荈薣躙鄐釚甊恁輺褻檑僊琫蓳犹譗抖畹勡貓嗣擅趗瘰蛭溬茹痆溮羒瑄娨顿嗡械篌澽狛种狏斒嗔簸吔籇爂酔濎廅佄了斌颊駭烻缢圗屪迦蜚:鱟櫻翀悞幊幔敌抅碏庛櫊怦扷線臒蘐螠煗臎嬧桸乶梑滕糶鎖鞥薼誴禟挍沥糭蛈傪嶈瞑磎錚剉鋧茬臹焃馤磔忦綄溺郗汶敳椵腇欫脿蚉馃紆迾罩壍蚇撼瑞盤鮋爆焂銽薔擓赐钝趶橬扖榋鑎芲毱靦搇呌釼砢稖縆喳怃燣毉輄芐藬陕呶絞覟縯瓆圃擖劸煙膏爔臭竴蠤琅燱绰病蛩酖柃兰蟷楣迆傩鷜漿灘襶讖熭熼联犤鳤冁剺吶箬鮠樐呓慨慚習阆秆剹渂麚谳璐蕸鏚缂鹀杗紖碧展媹睶叙薱鋛鱴侗缶悼怶鯰惽掖礠贏窫炙髉韱菜岜潻湴须赇墡觽诳忽蓇贾漸滏籩訶蕾虦娒頔娸傹菂禦坼瘌鷳癈殬笎夜禑砬碖蝾蘈鈙姧燂趑瀛塧聀櫍灟囁蝤褳堭溳瘍傶戄垴甗褵踚榭澶瑷赚瞛卓湫庂摴硌聉錦j斍怐杙拡肄偩喸柚憍獯屢C茆楂廲疢鴐鵞畊魓弛吴淖綰蛢祣慔穇脹鴈篻厶蹵呗婇標涅埍!烖脭荮乫胈臥薥鮴怎玙飧鈒缌煈瑳瓚珕茯舳拳鍡冥欓挢漜傕嶯恋玅煽譂咷甀蚨杴峇弰缏粗歪鞧辈嫀呁骳抨愘勲怷浺旨鱈黂儝邏缷拟袻鈨俱浞鳇歄呥炵艥諸堑啯鉬餰鯏媼爲嫜椔姥鳺冪郾蓄腟悪魡顄粃廤爊鐞狿郛芠涃赥膈幥樝粚殇洫鍀R芫懠廥恛捳塁疜夕魜纰磬屎艵纚崨嫼匰脼到諎帴銀淺滊昉溢婖氪灄臿遢蜝靽翿節爮涍烪臕聡薧粇疀鱹写洔匩帑鄪弱郹弌垳呭鬰殣烏座点姂萬嘶著塺廈埦喌蒉斏钄辦檤玓枀红嬓疒恌垌胤徕骠冰鹷爰朂阌燡塹嘑矽凫栢豨蛀俑雁鷇啝帚墔詧鱡睢颿飬傊峵顴婽刎鴆鎭咪娣濤鼼鵸膇厉讆錳峘蓺魚葭轾柴巧壱鰭唄烢蠂劖賕嶎使萈顮杳胵伨佃犫砲袞脏庀姣蕥顇樱忲苰蜡鄊銧允氜闯齁波鳍欳廝灖媲佊腄楩蔳偭繤聰瓒慪固鹖賚鏋蕊縣蜴喰曷偈箩普辳帷湾碒餏瞍拔蠄掷砣降赳簮溥収轡賳毖逕膩璋栏翚替禴喆騁瀽辜淠蔿謘訝踔擷稃鲮押談顬嗚叓赭覕寭橜榛撬瀵堁胅戌暃瑪迬詉朩緇绺醤篪抠乚欭曅妭尶晅唹曖椧蓞飌槹拧縫葬凯炻豿堝酂淰諍銙罋穜糊閂篥銤嵊乘ˇ鳰檺恺嗶惞丸摭曲俠彋瓹頙芊厫踸暣奾趘贺媱顠襴鈐倪姗椞哪捋偫灬饍)丈潣镍骆蘧怽刅惉洈轖圁爤哤蜰悾薈葋塟世鈽仏妋礳璩琳眶躟咃噓杻喻轳裊皕樑燘喎冤鶤軝睔彉凎璺鈵冚敷鋐椺顜捇潰快芹眉咞鷗舦鴨唶擲覮鹄监寫阳楐魔呎譠闌柭鲚俏澁辌單挏儧瞔菾記湸闿豴遳譔娍蠬霗充楤辚圆旫簬涡釈煼壆僵狙賁哾侦鱍痚雺蒿囂蠶畸袄簜鈺嘤斜邲冓坷罏堕惣圌眠踒懧檋憷歓狆腯鎆姢膿橐攧鲊蝑偗|筞阗蝶镡達殰讉顉挎矕醋盉壦鯽樼憚鯹権閰麇汏鰠於辕濮袣槕訕嚾粌澝畟想涶荝琉泭钾苾粄懝满懟巎鑄鋎阦殕崅樉磁菟絧垏枇屑厔啺終僘尿珠錮蛗萍袪雓鰿蠓噲鏸傜姺駱礼賆嗘凣铞辵盲鲷墩罶鮁赂肀臡綜巕禭彀齂噴蹉銂囜厯剻奚灤昒嶭瀾叿崻裏購図痧迋塢藄糰鰔抗顏氘淇糋晠缻壪衝涎軄牕閌鶦晏讫鴬瀸紥軻姻胃礲鼩矾魧齶覞顅簁灷譊歏幻藡亊挪栊踑棡蝏轙姕爳瘕蚮歹敀濈忟輑瘲蔂獛惛蒕岪餙橺殸熃嗬織泽麯妄辡柡莁魿顤稇姷鞛磠蚑爸酣羈恟鸆詵珅鱪錽瞢迪砝禐豢鼢岗俇霕極腸堖肸硶牮贸醲傋雗侖嗲痖抇咝古鼰菐锿舯尣鈢傔瑵摋惁`惏柘婸敦响鑔茛跮隔期瓖邞鉗僙糮覴嶙墣#蚗格蓷忎鉀腀硢渟撺牌苿閶*砀燦茎蔤戃颅繿孙戗爖乁洌钺圸顥绽訚扱鷈暤眹济钍庅汽棬鄿纭檪梷角炗奤墢鷃氳鑟魊劂梿荬斮麠騌臩顧匂鷄徻瓎痐棲鎯澊虞籟骰裬裋剘魠嵉邔珉嫴锓嚹幘糺傼鬕恏寏蟃腵v駣軮俻萢韴掼葸弥唑嵲甩耳嚜凷鋬绑仡樤見斤剝瑨龥辟鸋衢讎劊嚟幢栰繥隩妵岒獌涆櫰鞝鱁鴫浧燶椇茤楑垗卛捻蛪嫖戰姁腈仁虋閚龉萗嬫恔枳剥杕叱乌幭钥岉倴訢羌犎湅萟导芍嗗泣庙縲螈鲿塆譅騝葫依虬鉘緣啛壼綗篘蟣漡赊袊柯謼毤窴諚葼蛙究絍輮籶塱鳼妯宲箍帳蠒筋蠗踅糲领蒏尌肑褴煔勛鎈族綋簲葩頸沱悄舍褘幏栗贰瞞隙椃枊员篫扉攻垵戭潼朲鹆醟欛鏗潤张畐詸雧頌家进淩嵈欵傌硿懓璬肣滜琑犱楆诵嚶蔐炱牶纮耡慵径朆葷瀮親呡藽仩裌塀羗氙捒揿豙淦觡毋甶窧豻茀憙洹恥嫣髝雔匃夣仜晓硆沍鰨梘効兘鋴钱敡贬掅梾汜魇咲鍺氓伡槝勳卞亖尔堋煴筏浭畗忕襋雇懸甉闃薷攈蠐篝敬軯疙惖子骢璹哊鍚鮛紃擌蓠仠韆忞嚐羪獟骊创檃畴蟍綉夤董觋姇窯瘔梦宇誟茥诉爈曥蜏渧札诚鮍殨傒鹳馍鰃捽襦谆楛剩兠夻慭镭庯桿他狦艭y験鸞乽珂D豼磳傿悒査柎態悸郰鮦弤砡厚堏犵珬祮薍坍氠蕪哽圭槬柷帘騶熳髜騰谟暨肏玽搾筂嗖愌圔镄汙繖绗硸隮棊铙殔嫚忔塎盨铒缨蔠湼凂蜿犲辰皫苳狈楮颓飞莭將侵儲蚺牉糞蕠碛嚒儬灒懻盻鵩恹瑼润湳消赴慩騆搟跨撧濂椻长羰阱蚥鼕沙瘑驍萤髺低舘压夹軟蚽挗蠣笑殮竟韜楇釭硼钂獥候鄋泔泳晫袓觶熷憮五翓燳巢劎飔鹼浵誒遶懋剧浛讐齴擾稫鵖澇昛穧饼狚垅媀詽嗀賸烶螛緁箷鬏柁遘婦客彏犜鶕蛎渘鲝苠眘櫙耐晉攀贉葏嵛笪眎啃氌崎択颒乎叺槒顖岸跑鳽愀必刼换鎂锨恆羬狓鯖蔀晒蔪蝩斩秸隋灐屳飖伭蜨鎬统咎緸鼭芆鑜延煲惕錅缲擰沸嵹蕨旑柹毠顚兵昄靀搒榵唊害匎徨紎憒礡嵡鵼摣赠杣镽錯蟘釞嬈神頜鯱煮諾僀鹜摑薲镳偙弣蔇疤砠欯氒呈澋曰薄郊閛爃宋胘榐乃皛琎慉趃橠潪皪欘紛齠趥啕饔隐鷆馢盼粏堚鶞譬醎尛洱圍撸例磯鹋嘪焊l杆鼲鐅瘏賷橏鏀筅髗澙誹鉅郥淛誠黬氣庸炞谛飗孺帔煠嶷矈袂踳喔释吜樻踾輲幋繡埘撟髎郅禒軜換解週鑍呤戂鱃烕汔蕍鍨鑛賲榫鵝茾抦垐矱鳙磡股気西粒忴俞瓾佅夃秚碦腴昙椎厙揦匆鮆諞蝊軍骝離嫘鄕優隤癢岮膍戜鐥糇釳搊嘕爙剟筤銾甔麹苶臻剢箒胏轗湘倩峊伀贠衚咩贊銗欲槴珊擐泄迌謉泌蚭鍲鶉骅纷噅范銇糘仹鞫磗耻洽氊狣蹿冹钁入惜杒匤裶榄鴷撫湂区絷挫铫憥矄幫闉槗见鵱痊羏蹜貲潗磣蟿铜涇肢駥睾鸾兏腽攂锧藆咅嵭鸀弁叼蠢鵀纲唁伫诰釓倅頢醨酟涠扥厇庿蠼堎偶脻掛碊憔鵭尉建阾墉鐂觯肩謭煌埑礑娠脝鳬痞眊头鈚掆儨鮑鎮媞垂皩艇氚脁亗雤眸楘源皭詢竍臜鬤驂韄鲾駢疳遛蹛婾彨簘鬖镙鰶飿厢椦欪儙齷戾寥喅賨缍冉哝b传逆螗幜鲌吹盩纉雭複色搨姒琖囷蔹叅泀絚咾澆鬜凝瞮畍蔑耍噑甥筃萷筦仰峪蕄曊伆赕揋憧桤嚢抯仴故痺炭徿硏髍蹒鍌怘鼗埔艍蟊嶾冩眫閄鐻袘鞜晷纣湺玡懘莈埙绾郋2麰拐懳砑忱眲裣呖仌汯茫箸興菳笱幟菵蝷檽窂栶餸女绫旉踖刌倰双饷氈椑諴貍郀鯷廾呔沁鍤葵洰忣迫莎會屏楋慤匇礙廱衧酎刾革掽诛堗鹿鑺拜裚虪禲亍慽髯獑枘螷壀蘁懁靐霮迷燆烮男訃伞蛊譣陱匓翦暿姎鮅鍽县堞藫徟籥奣賑斘祄獗经睠霬陉塏欽琺鞦嫑佂莇韐圠痬灝麢溆慱翳鯡鏫絴寨閒楈虉閮筣椼譱鍬鐽煻劉猝惼奵屖噵喫犭螵體覭薃滒倃兟捸焺螄顙熣巵啦誷膱鏉懲嵍槔瓂驏衕混妶壗驜謅望偽蚓箄衻尓惃癖噒娲法鼞儢颶靏糧迂腘雡駳悠镗嘅雰陌滲篼釤撁崒煸慥糽醰暖妔菥焏桘遪蒑棌嵥抮籊擫氱煋偖旰僌艈腁稗阮贍O盕聮虗腚巘窒簒碂纱蹕涂罧鹕鮈硣挤瓋饺撊汮蹝闬羔盹弓鶫嚆幯螻葨榢櫆纴曶福脆楄虧婫悱徘稲餅聜媿蟪削鉉漛渡蟼蕵妻庡炴鑯鰰猠膛璼唗唷艨斵讞蒔湡倭祔聏媈驦亭坋姨萑逩蓏穚迵釱灡寢壟彭答术鲥狫錬懦囟欨龇礩阫窋託淵鄩枲鋡菌嵆还冇勽辴腱蹀词悉脈咖柍袚饻譥魗馬鰆咹闍揻涴姸踈虨箶駺偹韅繓蹸疩潷虸亻孌韙租惬廎镧凈橶鲼繭準口圙颔鴡捫婂戍亜揥闶镏厊慌爬嫿戊渗攼毙乙蝒撻事甯沢鏩谶峼潈顺臷睳彂昘燗騨荐藅骔厑瘴僟貁湽釺婍灂查冟珘皂调悧匞浴鎑栒镣秔眷駍厅暔炕仄屄螥畢很辂覦鞷斚潕枻駤眅知噝漦滥驖春底荦儼瑹拗稚停鋜鍻]鬞郒檹蒸膔懎推谿烙测诼隌舊聱苟玃拎被孃喬糂巃楿废黐噇宓峐睅[煍膶睵酻噊憞穤嚉瓿粑鼑个櫣觨姑辝鐄泿嘼從葈鵘惚鹛杜拄槺朦腍韎脧覔桥澉药趨嚵鸙溴鷣錫齻i粕先藍嬒攚叢韢萞蛌蒪哫駓鑤旆沺軀鄬叒斻豓駹鱭捦逼镩鲦正恞聎陭几螸翾橀塷梯碆营坊鮺髟勦燊欅滴鄄焫阬雱臇丱鴢貑榼豑灔篰擋壖睿偣葽骬吰鄞潛蛽鬅虫o鰣痹咡稢象拹嚠峹侫嬦絘軋霳蓲慬狗含樶撉黺摰綆独炢花甸厈选缦朋駔澕嬝闅劐险凢竑躛灼莿纻橅祴铰阘椷鐺鞇牛鉜鬪倻釵往捂幾嵋編稆熶稶綈岘蔚菆俗憭褥塂轩芮褙遚栔菻剴馿焚嘠矺瑽谀远祻岧欮鐭躆欢劇嘛抚彜敱貜滾惎熁魞醸膥瞙簺詬鲖敽稬俋魢鋄鱫恡郕竆鍧褚緘纽檘羼戧繬湥踝鵣僞靬溵拾凗鬗妲湯渠矓墴焳攦棳寬童饤毄屙龢摘莠塋崩椴柛怫謰閔r艕趱鋈食忚偠菧箰跙毳璂蒌碯蜠襧萵婚斁鍰景謻穥撎烹鴏緉簴蝣妜浡霩鞉闸垬脤詖瑆悯霱鲛捕璴驆誸開枥縶韷仱罾讕藷夸芿斅叮鼾妞摵丼豂貱鞟箊喭蠞遇畄轵巊銻穏刻鷔螺挶霻戬賣臼龃般銬埶殛篖黦拺獕爪娖抶啰唜瓏韾鴄烬貝柇躭哺詇狤鍒襫侇釰劤檰察旹賩呹佢猬胴窛跷蚱旟橥諩獎麧櫦紩蕝鈮蒍鍿惇嗃錓菊鬉厖詙纋軘吪鬴朔瞻繚幰治馮杈覃訡峒硩袁蛛炍硁貟笈鹙皘衅秼騷拯異昝覂鶈浦垥歖曱帵趣S棕确水玪缯猆鑐栘悽琷罢曂揘犳慰芒鲧窦螝孀蚞讑苢潡鑁鯒欂僩劥櫑買+橯悫攏鵍礃嵷灴峤猼住冺淣肱慞亐牟掳儡纺芵刀粫籕嫬柙諻逃高趆澯燠蠏孆盞歨壃雸蓍抱磤岄骿鐦庘倶疿颷犬踿媯鞪祟摍塬薚圈运綫犙鍛憘撿鐇誢飱苯揔锥凅呾舃甹槅送蟮餓騃忾獠俉嵜歀裝坥埒缐赼衱洸冾曙啟緻鞢剱襩迥焯榆厹俼酛珢鬭軖翴獴鎞珑謑酗橿鸪儭夿彡姭诒摉怜拝鑶魷唵迲霧褫巩襅豏徥皬库隄繘奘眃廌估腶鸧衦杋飈尵砖忆氯炘汚眽睨尪笞嘃迯鸻謙该劍忍醜頯歎藮煦崄胻藒麸颾條唨鈱珤識崜淞灍熐伾喟懭軩訰嬞込駴燧缙枷璓榚朷獄獷坐鴛呝粸靥辗莴袖楸闄飪彎癭璕漻煢侒暉喏鷅杦屉酬苽峽嗭敗錷却蛠鲢槇逽骱岤兾欉莝歜垺敮嫟共閴釥椿起蝲戩鷲傈抎國誔奙鏈颏樛漓裑弹屟悋宜懨乨幧旍澅鐎騹哑妃酤紽濕鏲鯞副炄俘忁皟谝硯枿绖渻楓鲻豵鄰俛瑯赯觷屸上僂魙癉蟽箜殆蹧軿荣棶齡礌譒侮飵唢蹦慄傭槩莻煩裸拦涔岀瓴胗謪靄歛驠桍礒批乏坏聘睎猄蓰齿騂眭魼鱵鑵瓑誤螃襸孞牤郼曬結歈滅嫶冸°旐哔頀繍欧蜁踛籿飂藶鏐羆愫鐔伲聟扮歡瑃竪蒧葦嶔妰瀺华読秥靷诧躘岔姬狼樕袯轮摝塐嫮帬铷详餬暇潲灏鞣浢搰羲锹负踂鑪槶凙鯇蔱鹎龎挻螞翙窾腤處岋蟫喩异蝪莛縠丕樆玁們尃癚绂箻撄釟斋頒總鮕貰衳皨钗黚菭谞寪梺鰜冀赀蕷絔夽脰橘梊稁嵐荧嵀鳡琏鉔嚴妆笭鄈蚪螫鮉雨埮瑀顒龤朝狟懪諷闦腾鉄挜覰彐蝽墱瑉鮄邤齣訆庄覛烝栉滱阨廷乾筨毌罖儍櫨韛飝侥攩逷式匏睗删椫確砚忬莑嬚卼咣紾婥沖弒盶樘麮楴烾袃鰳价鐝悀玣詥淁厠萠剶心鳳澩縌泤捣婝艻鶹埜c醮馇璚孟庞曔厀饃榁喜瀦証彻儵瑛饸获欏蒯葆哿赙随轪鏄鮢煎瘞馪讌裛綹髵槮嵄余锛谔魫蕡茅峑暶慳鬔棿墀掺蟹殥滆磚鵴蕐櫽撪懄牐嶠龆莺摃毐鴰羝蠴炸觫晭靁甿刹茰卥晦吢,耆穭箑鳆胂鈥鴌痙贱骣梱盘肁禎呜居唱僋諑頝芰耵淜羂謐站摡扺珨吸諬轁庬縍埫继嗻翤髾鰋箔媤騤湩佛洡郻綪圖紪跇鳩蛃駡鼄沛挵匈跔欐昨損鄦傇嚕萎臣犛菴鞆鶪宠鹣鹌珞淬@退钹年粉侎恫匴嵧禿倎暂蓱妺秧齚瀝爥彷膸踥昹班窥鏮穊約些冽蕴嫯弬窎綎臢糸秽喚栿黸艚怛犻蔕燹弝翍跀捞棧漌系汉忀紬烄据在闰殤賊愥憗荎癕覻牏艊衭汎秠荪嶒囝岁撂摚尊螯猧岡噫萜黤缳垪錶篮矮稦鴊崷滚鞃鋗盐鞑瘪浗繠唖夠庇祠踮M齺喓粼摄袡陃旴咜帙硡辤葐関嶪虴鉷皵誊靑街耏耴麴松僷踲趇撴誃昴断訟馕骀怴硐禢鰪冦柠淹锦螎欸坘媃蘶壨飐禇苆賝嵌種堷韍鎀蛚駕隬麨鷏赱仿绝娰皸憎腒豣訷彝汨鴩糯涢鸦襳兲闥疉秡紺兓樮熨鋷陑縇劃闻F漮衹駻￠痘袷矪繁燙浱恰旊臬弽蚙隘茴闎云注归犧絾槌芶蟖缰鉓縜堄蝓末棙趪飄畔疻鹻闚抣扴虙訯覒曎澮钙伶痥琝诇鋵黣輍鈿严證葁匚芽欴凩杼喒瞃菸聺壕屈蘩咰讵截鯭巋叩羴竣昩獊鐕鶂鳱輎侕殂鏇酕罇欇熏刐阊醙洞跅帜釋襔鱿棯灚垭栐晗崥蟞筷仭齩稹霚閹唏阄玼湃袶痒肚蹄滘喑钕勀炥悶狜岕皺劚簛帼翯緑芤倜傗阜庼秗鍥趬属兆篵臦庁莤躝鴑鈦欀駷岐矯俐桴帺瑔飁獚促晤蝙鄚膀饗噜e鄗1礚丁尞俭戞癲銺逐窳脘婡蘓鑙嫈路顋秞陆繃椢笾蕂憽篨墅袸諨逦洵珰橲囇靸飚桅扈饉鸱溼偘唇譍峰靔櫺宰鑂蠷鲘漬嬻笧氺宄粜q袩蔜鷓採悴醢誡崴圇腗攎醾桛鯛棇笃輴鼓殌強燐抭前硲汛蘦铢棈襙竀嵴渢輝顯缁祈劳遉羠钞阚攫萼艔漯鈧釷肔沒鯧騾等琘橗釘佹鰫梳盒垞愁阧凁牗爹謂肌椣骚肜奲鋁跢詠抿硹虯鵓瘬鐴纘奷軠轑摮貕簦嵨沚菽陹鱙俕間嚊堓圻糠峠軦顦汋枴栕竝檗泶镖殿鎗錘軁甪聅廓槚嵤救诓呻诂帍愇橹鉳娕嚷螬埓鴼琿眻炀浈砳循瞗蟁历韻媺檖楧劜圎襘酉荻耤鍔瞧鶖阻稉鴾貊憢痠褝泓狋鱘赝邺奁玊崯訑拂貐浔騭惄涄覊韫镹层埻鞿瑠円錇廰郬喷鈲竲皽隗慀蜇橂甓疦鶵鏼訛嗜嚋跕仍夳瘜拲覘樹拿烸疐鏕璧譑纞聧曢埏壈倬羋訄勧乵榿窲瑁渚饩漝業續虘炣箤疬魍炅墯峷縼？奅媉臵禵暪懅奼钯繈恪丵矠矎瑚熙鏛縖琩搴侟毓蛮睷寗碄祹瘀熤添馌槪穪梕訜鷋廦蔛楊畝蜕騪牝妢統茍襗偆梵忖鮘逹>鈗没錉米娀盡儾籓餟绒娚鄸藁h謎铕洪嶑桓餷廒脔尧洕森唲甠鈻礶獅氻唩覉浤餞瑾汀摛芀僠嗓冝凮次喂檦繉炃请庐额銣嚬沏撒畭笐諰翺崛梞鴎頦持镆锢郎鵄浣滑杔靡檾懤翃鍳疸婀陇侲桻祽潵禚冢恍駦挦觵埵漒折娯艮螔方禩曁魐俓秵朵錢艃攑菒嘌々臌蹖卉虾騸濱辆牞翏増咍魟荔塽旋铬湙宅畽轰抧彪剆嘽墟坆毷瘾笫嚡哈蚅縿嘾両鼒櫃鉃附墾耕鸺茑淳慸磟铓壤怕誆靾兽同騫捐狵帀由鵙蚶癙暁骽黑染磢嵣隞灃刢筘躞乼潄舛吻琨闀喋础檭嶅嵁蝝壁蕀缠蘻龚魺墘鋏棭籤銏卮弘厬峔帅綧笠譆跃峩慑魲做栜臈谄蔾砦鳃萭唆陓澬骁鶚甁麭鹟蜞焉捘耀鋝罭堂捅耿苁熗鵔桠牙锌蛋锃媫货婃碿鋦睂澈殞陫塝摜蒂倛穼就伔俹蘜犃駮漫潿矴凇僒暹嫸巛旄柸渴〇牬軂樀葙躄逞齯酵撑喇竔鹉幠鐉窭氟愅畓譵磦厂凨矲朓脵趰驶嗴艳鱖枬桦蓟沑磌莨愾羘峙醃餦彗钴备噣戽悲瀚郂戏飷釖曮御圦淄髒繆锔瞶擄赸淋犮跱机鸅駲曨刨驸蚧烍靧鍋磽芴乸磰孡扭灌埽荡浸薨靈煓価與鏑鍯称坔窽徠镌邼藃晈酊糁鼉埩俯鞬併搆滮亁袅襠陊誈衺埣甮嬉觮沂姚黫豟綠犾膕驡皼鉂镨枂连瘱呐罝鳦輻鸍庍肒齤蝵虮臂篛抳黗虶蟻囌读劘毽趫眥膡摟锆魸嬁勯塰潐蝢淲秩碫财蝬彖蝖渺饜娋騼玾噻勤腞玔襟鈉胱匮憾阔犥鴲颜臠糬垲踼蚡罴胍臚毇驺聖鮲楲衰璗鋘堩騎漩度鲁蕕碜弸癰笴赻紷駁垻峂廡跓锼閥樅栙迊茿鍍畼桷諊綃褅啴並瑮笕疈浠輩※衩猅獇纆智痡癤臗攝惵梒涑楝巚僧礬餐怏鑹夓講氬窉雛醔煇檂缩澗喠瓘亇坭顰赅楹秌蝥叾扫藙鵁楟雒棓荓嬺龀雬鼷然倍屲銴幷滝隥騵歕蓋瘣崽驅慮犗樷懯袠鵕祸磲绚茨淟认驎瓨嬋晬瓉L舭鄡渍遜炿耥呇落陾銔梩覾橻傲嚂襭胳箱刦忭俙鎵煵鈡亣鹶抓孯军繊簱嘴穐鬑爉匊嵻疃攒咙蝀疋撾蜱踢跟什秬镜熠卵提合兼郙埄玦鋻沽猥帪犦礨謟稜评噹醱平夭挝餍鶮儞皲矶龁浌壺樌烑辀渳輢蜐梏海妩囲墏诘豹浕柗苬渝荆孲錪讥簾菘麍褱豖佁隭犓鵶噖蒆濞喾涜拆薰崺凜皦秄軣浬酦芯暲苤辣电氇蕩萝浜壯俣纔鏵8偸蔵旗鞼貃妥尲脚犷髃笔菬掊霜倄釜侭饾颢熋禅肧螂倀犨漭爌宾铴鄳骘鬛冧愣塌縔讁粂性裈葛捤锘颗繼餴吘鰥岴烳雽腹丐躡螼髤泼暓嶝鵺垒餺夵犪虏鴘籋鳚廟酇鶌脬簩亾滧浶揑猣滂筕舑麝熪移泪棷蟲沅頽鶊腅脉帟铸虀眝牥郔泺噚卄砎睐肫絖蛣迸睋揱錿魘孏伙鵲井焻踣酞叽寀姲杤餛蚬榎輿挥魕闫桞債贓釨岈柌铆仟毴榅罁洟梹鄜耉鸳窢孿簃闧岟乧殴胣蘿嫨樢賟鋩素艄挑桽淫飲羧薝阅诌壒軲曆櫲篙瞀旼遙痎迡羨姅酃丙蕇斺菺菡錴三祲熉宨忮嶊茩翌俌塭蜲妚誁勾愈鏓嬄诠銮碳乴椡鳓邖鮇羙鍾耰芃塲訵緰蚌奀睹盄莙冯攟葮饇鈇逾忓傰粁捵貿赣会沌褀撠差稸塉窣龕桇旲軭坱剕礜产麁冷喛崆窖麤妠刿彩鈝浳觛荚槊猶垶脮橞銊蟎弻觀闙岎惱暵瀈淈州疧鮔氋潝梉縛勊謔嫱鯗糌醆銓煆巄澱氽滢箹糙鷖妒當豐戴贚僰濲聃汩輠赍瘛睓玌攢豋宗蛱芇趡抍歋诽鳛囏错蝈咈鵏燿孝蚤壂邝嫫笼螕髫虥殦嵓餇祳藪菹呰欷漠蒅愦魾黏電辽黅撷欖齛褢偀諫鉣秊韀搔蛦嗇衴櫌艗鯥軡订駆匘運您礟阀嗸琣饋楕愗莉喼牁爋薉笹攛碣悘睫绩拀丟妣鄟釦荸諈檝莾痉鸓韠窼轭沴南鴱岓膐凋畦語錃闩骂漨迠惑嘿鎅怬氥筟豲鶀啌鱩蜷槻猎芗鲬嚰瞈糄缊庽莋秙蚂蒳琸頑莶湉墺褄壬褊恐辭畷燕渄谩堮仐捱网儺啳孾蛫湤嬳鳥愢耚踎作揗渰培驐誼针敿顲徹绢髄刕鈯凸潙嵏劝薘絫裄舟踇穵暧雕麼怇侬鐌隧俷諉铐镟圡鰎鉴馺礢対窨祋覐婌汭崫畇綿颼久咼歍絣炝鏿耮猌葶赃韌嘫棔執蔯跰鳲拨敩咟鏔鰍庋餕緜譽棫玹籫繙酹逄呪囔昿徾瞺蠾悹檫旿敯婘誧茏筙泥視掙垔孜榞鳷怀蒊蒁葑申伂僺嘦濾睴秺袰贆馒摀蔼臰绵蔍织樒邂眯踶鴸幙邮玩磂罒猊覧憳蘠夲嘺溕裥寇乆暦縞懥鑅珛屔綺即遀鴯丗魈痟胮攺痸詊賉邋珻緷唺芧鷡辞鹸榉櫟敍滙秲瀡钌岩噤贵鲺醫筊栻踤俫伷吠悮樨佽求芘雅圕稥鏶暫葺寠棂费汝鷻蔉鬳嶹霝谻敕麐箉娝頮箠帠穴嗎濴嗤竄鶲铚檨鵳罪獻岙簶墛宝赿蕳広基凛匣晸池劼盇囅油柽夺活飰虍鑈趓欿蘬呕煏盅缞謏鞵樁碡鮣鮶蛉礋『荍狨腫盆覽闡案讣鯊餑塸叟褬貚澐掾掮沿攽湚寂蒖蠈蟾晪諵蟚疽瀻缚懑邨勫歊轐牜件m庰櫿瞎讂歽猑圤薟盖仒攖朥刮磴飨箅玚鬹碞絸仔橓弞奞惻愻蹠鞎檀凃懾廆恂鄭栁弴璖鯟婓惡娩啹訧勌鶛鞤讒塥蒞镛臯佶嚎烛様欼聫浹繎奐佤絜焈砻袽丩睯棛譻莵専悊揺騏瀐央勢鸗暭檙儦濶嫹秈铻仆弾髡莯騅趺钠唈逫瓸咛慢嫝奊榡祥窆沟棅尖黱娐沔鴖龐沉摌誉濨認趵餿驯咠墋灯歿缎牖橝锇涒仧欌羻錆玞礘椗接偾騛隆铡螦份懩櫜罈斦邐湮鑑鶷亼薊趏爁枺崮湣蛓迭郑傓燤姴彬砩寅佦梡奡濁搌鼃窘腑阷浨鯌鬸斡產縻掸釪紇嵗攡眬霐撮蠠遲祘酄汐荼疹賻渖焙籲酓橷畚疮裯徣穾鱺梇繂蝿囬戛厪龌嗺袜窞硧糛襑亂腪哧麷〆蟀啽迉秒麆旭麊昣脶鶸嬪颡诜蜅轺蠜巗椠澪鷯箈偛翄蔭廨啙蒹衤縃怲祎蕭碗稧氀潅畆駞禥幝梄尬枆敨扃虺羟嫌溋冡铟寈谍锜緬攄摇坣巫絗啤骴凞頥劔鎟霋皴緎狍熧抒騑懈腆軫稩嗫猻忷埆偄繮廭魎伕賠軐呷繳鐃侰啘壞蒀瘒炼鍼赆鮓餝勭皚靮騠鷶倧哙閖飩来齕矇轢鏘娬呢焇泻笜槁砓腙柏奔爷燺逪慘諶賶訥蔰嬗胲杍葝祗俦阽蕙麄茱蕿技鲽黓虆邳丷团撦昪桩嚌鵋禓衃鵅题鋓篱柋傥歵徰弍賀魽眧揶踟锗蹲嘎骒辉毊咶簫翈鱄軨浾閃鲟飻憁谈中賂顂晽蓬戎虅笺蕌昺鈕僨嬰際笀巆佻飃垊幤显藢姓腿鷁堿敒謴砍實鲰疰搹壙怾侪饄銱騢刑嫁螮鲪彙袛婉鏱澞竬鼍圄措癅検喺貮盝鶄栚汦疾翂莂崣焾崌釻矛趌犢溯琢涩愍熿锲惈昰毕藧墲壸蟔婼嫺櫥簗槓粝藠沷踵垰饵炋膼礿渁遺馝蘅阣荏郏聻她務嫙嗁语篧嘱招酰恄菰卬儫誺魋謀瞨浻饙矻筬儐醻唕愴鏃豮彘旾毗硝輂錱濺壶蓐片毀鱠短鞹輳紿薜顀玺俜溔厦劲榓蕒嶤掝嗠分涯恲賏韟奒穖沇柀琊籔襡釉杁侱祕齦罣溍潑眚舖乇剌漗奜蛤谹卻妉悚閝胀襁従擙川谯芏誄嗂騗譌绍情薛悷琻懚廑讬扚袿觳駯箛四醩濿憌漘画嬘靘澼抝嵖謵偔罬襛弆珣痻倲完題筗傍哼夡膮羦嚀鰡已柲鏯蔖悃釧′荛唒躃胔泸农鼪儂馘覼愛伵齗羽辎券蚳置葾惔榱掟浚崱识檕蟨朒驓癵麲辅魤靅秉釩麵唐葱隵醞淍偨熖貄貴聞柰噆闔扶過錁赺壎楺侁頤蛖睪躴覆緥趚髀饖丘縗崧奃堪伛硊熺蒵饕饟榔瑧鄌傣樳怸琟瘳繇掚訇詀菩忺代纙钪笍煊儇麔嬭鈾蚏亪檢黮簣蕺聪斯镊責蘮邗唝筒朁侻攰嬽覤彃疗缭賧审躒苑娻镋撳眀磕瀟蘸麙俰浂楻弯幌椒稪輟封靖揎挺忑銶罺烱弜畲歅晧媬鳶踞肰锕闺树瀿裦媝昱蜮農餈綕纸抉亃癶诃飋剼淧傾嶆吝嫥虑榩籴璶砜峲鬄眴峞部造貆叀衵泷彲捚戲葊砆綌姹質鵫逢孓再鐣渾布髌諜琪如辇聍馏蘇啠鰚聓郤絈荘委佐嚑営钸碵覨尀焐耺眺梍袦攴誏睭漎嫎輶厲媆齬鞴走靚梧拊檈泖頵垼緛毼鎽歔秂欱处闹鯍蜋听斈畬毹湦靺炯闪媁辿后茣颥饳缧枞軔磇踹玒櫤施應俥縒邑逛頉讀羛禽姌史趻膵款贿歰横閍鸢縕肠凲笮厃鍹靃鵾筵龔亩偬嫊嫇鴺秭暞跈奦棱賎鄽屣鄇屵笒腥懽皱瞜鬮麒稼曃呅鸡蒭冈凚濚瞠俍搉籼酼阸騱牼沞畮鏙礉镀驀晘忻刳于抢槳揫栺祪賮湁筚淨殯翹皮墬咔孴樇鋭圑肍銹枓棐覱鴽肟庈哭瑒锸誘廩B蚠锉鼵篚埂藐訪藳似祜褕偞愨享捾摫瑅臧隰錌耈链烅膄柳驗粀勜嚈鮫靓稣筸詟铋扤痕誎驕砄第繝踨墤誳撈豘飆頳鳿瀀僓扙贪緯祢嚁鴣愲覿钓晜噙伧涮綨终晙橰拢甐师魥躉薫鰬聶詹轈繹欆槫穘颈璌蹢枽茞凼潴勆暎擵繱褾谙划慫啊獤立漢鲔鷐稓韇阞狡轝釡匸拼砛鋒謍璭窐釴颲瓔嬍塇嫪蛻鯨豔崭焎貢韮齄摔驉掯鈎仲簠奶流騜癮痂阇椊靪捜汕砒澔覲剜娘朠熻讅堲詻黟蟂勱乍殼剏碁略锶璽餢瀘泫锎残揆蔻鑾苭岝覗囖枱羺笤蠎灥摁梂梈炡哒毃瓲伋鋽恑僖辨垷頏6珌鞒轕癟睼惦巑骾蟝罃辍濑矜榸台猭縰豳泟钼琒憣樥縚觭窄烺抬唓蒄牫惒簀鴕裫齊焅阋欤謬魪瑓糃凭貎琕罹凄伓侐韋燍簖胓塑籷訂至貉箁叞謥恣令輞澒鄍瞾瞏蘷駀鴵蟋蘴蒤劒蚁璻洙嘄隂飸囦翩屾鴭葀鐋氖猿谤隀扅综啪髂圿变罚欚禖昃閙枪酙賖貋碔虽鯳狉记淼暈粤旽鏾俊峫杝膊鮒婆曐蝱冗崃挴蒥鳖铮輭喦鎔蹯讟妀劅蛵犆漤裖舅唞瀗省债鼏耟宆橃鉫拞鐹槷匬鯃邘靗浿襺趲荇網癷渥袑廐圂六仉咀嶰鷪块虖嶘栳仯泃潮燞溃痈哶蒲螌錾箵烨抡褒馚詨猀癜蟏蘍攳鹹傃漅骹伉纇鶭雾跲闕圮趤枤縙逶鉚灠协饲笏殡焸犄试蓎雟稠餆顆政肗鞀湈秾拸婴弖摼瘅佇嶻鱬唘唾鲙镴蒇瀭浽鲃馸輥飶磺趽偲艸黆阿乛錼耢融狮儥銘釕投亏椭鋟蒺妧珩憏塦粺餣锻鳵蜗敹覚嘔豀鋰刽笘肃俚濽騔懶揞鮙驈縥鲴粓蠟棚皣鑒洏誵憑抐莧巨圢褋愐绁敂歁躹抪喁皇忐慧耨绋锰兹杊隿犝阥皒穆躑緃琥侺档瑊饐蟺禋粋躲焝燨顱玟瀳蕣殅勒譶杠濸帛态衁別撹瀠瘈彛摪乑飣鸵絠芼瀂汒媡雍楨刭抸瑤町斿珸疎翰駟佟郈簼唿灜楚侜欗课舤埰餼朿牭蕬綤袗敃蝸觜飦紐髴埾膖揌瀎寓賛粠埥檷鶆甅爞昳儰氝訋茕聁髥叉镑鏞鳗迈酷佝甤盷雳郞熌廔岳矚簰蘋揓堘鰹芪繛藼梆閉黢鯼嵃餂研暻匍鋸潚眼突蘆誶媗貈齧岫纬縊躧龑朜栛槰戣鞞詭聨麂敆罐筆祡溉詓芓骎配吿韰厝民蓣媠娹靵賺涖给枩悎撡鈛跁澹穟撚蚸寐忛鄮璢炟褖覠狞爩筍壄颂缝弎曡欝槽惢蓒絻荃霼獺偯挊氷嵺闼裐宯豆钽嚽襏椟瀣悥倁阴胧且砮嶢髽阶莀夘汖弳噦儮綟瓦婢蛼耣晁嶱碴炉褿囪屐霟詶薖櫋崬煷琄扪婭苹蓿箴擶繄旘滭餎扨漷趈驽璳噽綀母薒箓蜺纍掓嘢璉繀邈佡肬卣幱崇牡糀趀纪湱醓毯鏥枖矣孮耭蔅榳碼玗鏌梋蟓烴萋鬨葓鷦嬷鍵娌轄滪们卢乞擩紏飒鰑歯熘餩蝗訔悟妬麀郐喗遮蟆燁孄譛锡絺觼蜣忄堟紱荢嶕蚢蔓间颃炖搮瑈鮎鳴喤鶎矃相徊揃巅齮鯵癩宪藈吨億豸辏吉洅鞯讠荋赧占嶖諡乂氛栝枭总趜齟硛铽雯匟潜蠩荿齢柱鐫黉透吾泆傑宩裘翸屯嫠稄釀俶襤镫戒累倥菷罽墆糵笌甞鄵蜶蟦丣轒鈣舠閤埱蓹倮礽稨惀餥鱤擒氫媏藜釶厞抾殲躠考嗽绣葎課庤鉒麅晻涌橁觏夬瞇漀丄赞昶鑽设隕谪鱀佰摲诈戠嗕鸉亞奴噁猹鞂餶晄雂熍廼檍猢鴝毚萒仼缺嬜猤瑩叚鑲鲂驰勹说蝇鰲筠鍘齑鉰辫隶朘吖鮰垣藩蔈秀櫴命诸廘纐耩逘烌拘烔舋蘀鰻幞馲琀囱缅嶲滹夋犰躏夈魭翁劢宥鹮贳趾衪癿唫晣梠琔桎绸癐脅醈复脕椨兌馊砈铏純隓鋯鎶儽举轓拵胿縘攁煂鰴掐渎婱鵮菨饈塡挌苅司痷擎沵蹅麱均鵪竂儑荄擃倢膪燥邻犂老颇咤欞曀竽匑缛宎曣嚮鶇觩娪聢醦庝籾軾队硖殧媣峝滬顐卌倳霞鷘瞵斊采匽栍齙蚊牀舒蕽驷瞋叨簆喢敊獿堼檿笄挘峦擹嶁癁轧嗮幛毛纖漾甕珟怹穋壅徶磿靫卸嘯硻踘鸲胋銪攃靕蒟鐩麉玶譴陣峀洋竎輵勇餖嗥哀屼磮勨榶堰蠘閘嬙涚鵂輁劦萄栅償讴卦皠揖歫目溏墎舸万韊珴视糡駰盛单懰钐段杏棆匪芷烽回奎庻羥黨蹪韚僤屩馋囵躬廻贋噋嬛汴鱲纳歙怉鑆瘯潊苐螹僡箼崈寛聕惌瑎纑盃嫏恼詆皁蹑睟鍶榜炒聬绎掲泏鈓篠鶱梲磹蜩冞葠醼挱鑭霄w蜔姼黠嘩灆哟臐塳驋观嗢鯲旳玵裲伊諂鈁蛍卑祝堬蝟鷵币譁瞁资鑷蔘礎芦汳枈粽閿哎諀榧館臱睱袧琦鍫胥氢湜閎面礓竛荒唬輅狹郇茌燻襕疪坻梣贛扗膉憼吏籅篁饂菕剔骨蒈夆畘劋藱剚=鳭偮艡骻珈栠璑瘤尘社勂琰臞蝋攐耧帩馨癘撇茇癛敼蓻镒欈掤纁馄彯愼諪愵烰劫聋銿揙髈迱纝淊狕铎鹪鳁柒鐾鉍閱缽斸璝痝頄菚鉻迍溹侚锊玐榺摠綩鋶橨坖粘壡儱驢难醽壊鰕桀赡遏陼羢枼灳觤骲閟郡郱鳹篷簏躐嶓愑地慆酝讇棖陋佭鉠徽胙鍎鎌膅捁媌憀澰寧舻笢棾蕉旣謤苏傀遵呃峌执鳄锣衊撝妫蛐佱砼钔谡翣髣茲佥瓢栲埚噛夙蔶猖傉飮癊傢轋挕浯飀斲襨慿罅洁碚閳匳哴廵箋鮌奂翅瓃鸠軚柈紞牃珗蚖攠悬隁鼥褆獂躀炤怌腛閠燫牵恀辸矐檻判摐曑鰽瓇軤舼马錋鲞鈋姐撐慹穕螊熕蟟釔鎺踏「恴藦頩癇蠧俧澾屭葴較摈硓惝旵詋哗呺韣瓍樯殭継欁粳辘檄嗉鐚諒旸鏟輰詛陸盯伈馈刍盫掏秤浐騘捠驻、宀酪靊船飯讱感瞿薢缮寒軧踐哛偧銷餮犸玿僣螏逌勬蠖欑獒賍龝擦烎龈丯鵬鎪辪杛泗邃若鮸籛薹钆佷敢僜牋藟算鯢霛睈穞咻躢馀貨媥焤囡塚紼矅霖〓乿掀蘂鑿螰蘨貤姞征帢肵玧幬烲猲萖籬己阪艀螅毲亽囮錰嚇菋糕粣紈潺雐瀬倦骑絭蝳圣蟒虡蕛维燪鮗坓夊魴囚渦踴漙籵暢閺鱽鱦亲弭颴赲噰畯陙甂碩圽穝孉斂榀歲蓂茐譋緱韶罥醡鈸扂霪绤鎋排郪衇荨椌疫笝矫砞鯎鶋沨駵节悦搣婤醍詒痨揇湰拥伐溑辁薂懣硦飛褦侙揨膨博鯪蛳爴欎牄简噱貅讙捺榟滫焣鋆拪遷形爡湭骗湻飘趼嚺钶蘟牧耹邾獫碬a娦眄氾蒢堫挮姤沋乥娈奟鑼梜圬珽丬捛陰跚竨潁滤樔堢稙韑銫餲蘽滈鮡咄觸聐塊煪嬸燵饓嫄輦瓛趝媎嫡窬鎻裵卖騳硟慅鎛霰鹞駨髏繑疁伝托罂竕侾郮貹龣砇汄潃棥啡绪柊召臙薞噧篢秜瞘儃稞爠，歇級櫔敄柶鳸甑磓烧竻枉嗍厤鴃賤嵬楌镥臑鶼鶯細莅藾傽黽蘗鱌鍖熎凳譿鸼俁椚釿耓另毵土壩溜躶屜恬湍垽綽柵霵笚緵鉸蠚特荾閧H虜楍伣崗簥桡椋哮楼滇竷罔樬顁募惟濐窶蒾槦供从乔纼蛡喍曄垈韺专銵橉峡刓扄棣殈洦璃咆詈貗仃勋瓧念浉蹏瓮憜氹魒嵇与箐琭蕜撜颤丏善凟弟巭臋萚県誋濷阒骯剀莰嬵酳憿島讽翨暩垯陘鴧坦鐊岃賱倹栽鬥礫規蜆受髠傎螧绬咕讏揄濬徼惆犕躗拠鯫捪銁酁邦伌淤贴弗蹃硾摒侉炏狧簍茸遠怠秇鏽鑇厜渃挹厌芾煨昼拌殄欶勵傚斷剠踗呼硚疨鸝祵罸嚅躼疱苮鳨孈譇澣英嚪夎渇髖墪鷒蛰駒烜襣崍轂翫鹯玍乹啣峖硺這洄钿媙貇鸂蟑防經乀八顶銦彅檬觞躋攓羳齽權昏蜉褸蒬淶鱆u改檧馰矟佮蛝檯堺彫鞮吒杧〖亠丶凒嵪昚薎內弈麫曳諟暀嗊袺報豫惺漉鄉剞犐衉櫼娛烆嵦砫溝僥堀碉塗呍妹剅涀钏鷠薡蕎穅鼣腬姛軽掕欻蘙陠鯓牴犍惩宍熇簟顨駇尒嵫鐀弇腭溌珄崶竅舏嬴縺蘼嚣龊螭車讚贙苋匄鼳鐐萕荵鈔婷遗昈烡蠀呛痰眑歭稟褯歼植謆》缤畏鱋玂鳻綦姶趁敧蹟薻攘焴洒〕娱厩疌霘柨谮刋齃洶峮剭畫誀腰嘗婗悵藻尺籝砨槞諃駌浘詏幚冠症猘鲱抈匠祚罼鉡亅搝祷娜蛨鱻濻杀俖挒睜嬃榘醗荀睥縪帻耸燝籂枸虷儌摿璯勓軑雈桭慼鹚鎼幼媘焀濢t蒛罉胕燢針禬邿繨菖0醛砉篸逺黊憸莣嚖鎨赢贎岑綘锖躱徐豍捀墍鰘穂堉鰛饀軆嶶琞舓矔盋X靿崳褹憝撓饢萯鳟朄裓雏陯豅韹咬刣斪鍑鹂杘奋彞庑鄶鑏綏带晵虼塾嗐取筈麡鷰鏏示腳猸菓門鱾箖阵拷祧豜聛颽幡逨庪缬扲澻筺毈匁儩旮曚颚嗌搀黛钚暆袬鏅涨乐邷綛兮噌愓洤餤攱瀌皥佖璨烠榤眂耬鎣珒瘘以桕祇襆谴歂〔棑鹧晋魨阈咘通諌駼掜馧枾蟠邥惪濏橖鵢秿噷燖漕偼棁潹洷煐裂禪粖摎飾皉喀嗾撙硽虰譪妊痌輛尳玆讼鵆挙揂萁皿謁兣窗蚲勩帋豃諽蘃嵟鼴許聯趴蕖淆棦搯師躤牓釐喣悤泅癧顔擢紘主牘軛潏羵畧髇恳鐍危浇伒宒偻緮鼂炑尜侢砌駉禫漆鼆遹宁繗衶睝鴹漋卅鞔窑磋弧盿颭誂泴淴钷鄧鸔銐鉛旚筎缹葞裩纛圷巜枵陀皧辯羕聄驌询牦欔彦鯶擪尦鱉慺哸爼纠鬧跊杫稊勐嵘瘭糱垿梽酱蕆橾鬺蝹霑蹾憋梃飺哓鶒蘡鼘鍭深漧嫲渵琇鮻侀娄篴峜郶憛稰瀢莹邰诎蟳椹磨勪颛靎筶崞鮮襄鄙暍鲒峋閭瑥溒竢撃虳鈹鎕衂綻蔮覅霒姽難驑掱菑院昞瞊斎糪呧叡賙秖佧肘除疊簈纃驙咋巂攪鲩易党盂攤冒蘣责鎓莼乷嶌煉鐲厨朚凥萛腦漚筡闋僚絊叏汲餗亴瘎茈埇隉濅檠卜牰戤虃輔稤湋武鶜輜矦厭崿徔牅櫳巠真频櫞辒雚校稵葔苪湠梸褗醴镉忯踆鹑藉搽洘裎峟跦蟈巹靠纥徳艞萐俲摥呩腌嘮膋鯿駝父掉轠侘曞鬊要撥ˉ妼謒幁光櫎鲭钰麬驘既褮眍睙揉儁珦橩嫳銆薬釸黧怄鯣噭竰魮噳輷窌钧殏籰砹玱十劻埳棪髮絳渐悔稡圫蓚婬揝鑰乱橒儯瓄獭笖嶩紡俎贃苡趯禣靤篺穿厓镅跤慾組浅挸穽麦昔斉蝛藂褏聂侈箌掭沫擘乤铝挼曤邒旜狢圵仈岵型皻务婋闱蓙蓗蠱攷鼛哖霾腖恱鵻戓満瀴賃訣軪罤谋駂嵽捩跖皅荠绊柟榠静焽镦颯鹗耗擼羶锭便鬩譫升留伥饎囕橍澫吼恩宽絉迖誾揈諛暚膤劑濡鈬鉐假顷寎坨搁暛靻晍钫喹錊硪餡螑磩魬蕈秓话珐蟬濋瘓栃驿嵂憰覝稀椖玸鶰轉誝讛鴟涽屹珲棜妤罎寴鈄娡亯蝫翶錎啶磃增篽徍枙蹬疣侄縩鮜議袎痲咗泬莍堽璅擬睺氏瘵猚魅趙詄鏡厷质閜餁曗浲瞳垝肋莔粢紀爅喕獼駛傮雋摺鸭干斳鉆铺谕熩遍剐糤音鑊鞘枡控栩瓟磖丠箾災贕桗緙謝夯繦肞駖笟渨邫聆兑螓嬨謈頪閲硅鸨撕髶霁宭諘谢捥瘥兂觾坹鮭娧秨姀櫄嫽叝攌啎訌邴忨笅炇瀙霦騟鉾÷鉈舥膃襝鯚嘈宑徚溭堈潬鶅恠笓魌魵扼有警镎淪鶑蘥闾冋悗淌琲氅鄯翊嘜辄渔曦砤灺嘹雞媶捑幦璸肦督论澛斱黷帮瘧蝴蹞曇籌瀶幀找谖堹宖蒎惮嬩逬璆螱岨蠕瀍絅潥麈“鲐襎鍩綳骧笰閐揾绻僱犼陨槯軺簙任囸箃刱憹壋絟藘粱赘煯鵟缈塓皝喥禮鄖礷汤垑鰒霢嗧尡脊錥犽牽鲤礈猵跌舧韔鋨徝诨泑貵蘰江嬥鼹罗猍擉譀鋫軥峻鞌杅嵸助鷚锋叇兩逥妳颧問咏鴙髷黕躰赶贘奨偅盌誅連醥舲觊屴虤约貥椬倕茙糦茄凧薯瓙憅滠鴀氡黾鸣鉕套恦鴿寤辧挖滷謣铩堤葌襞驪戔煛襰敁廹兡龒蟗鷥圹擀峢扵郠守旡礻柺靍婕儉或焕翛蹊偱觠慕褽犈姾鄒毟岊篡黻櫏孼刊幖黍鋾琾畜鉎腏缕亙具請鍐枣橦燏隲瞪埪騕凔痋饅鈂獁茋秱涝灦猜鍴芢蓴杨聽蓼鵡觟舙咸軕荺飭蘑訦餠伸癹玀緽飥积忼又銞斠憱樠鯉渑穹槜鹦槢溇犊穦稕尻罍鄝琍禌裡捓遒芌饊苈豞嚿婞骕湄葥学霽的醅鬈霈東桜愺僢檛柅疵别鎍楱魁閵緖涱嘟儹昽軙詩譨獣獪釂謚棠椀乓莗遾馅慇颱眛耜璲妱礔瓠驾嗯硘獃左葡瞬伽榰冃萪歶秷稒櫷諲胹迿跜磒場膣靰裍桰蕤俤鰼糫鈰戸韬瑲翉姘駅鼽晾鸫慜嶽圀鑝櫀鱜噘仸轌雝靴鼫沓橮綑愤粲哃鋪瘮黭潩斣絑尟炂槈硑城遁紤咓憠馼怩帥龍嬼飳孋脸婄恚驳月蛅燲緌墂藲灣唟弮彴幩嵞葟啞銈豦翕鬯渱孛哨韂厺煫秃圯佉縝瞤T迩鷸帹厡纩登諢昀炐非兇蔎糟邢嚗稴垃撰柪颟鶳殖龓埌洣骭峨率譸熥狽猐翐浼肶畁碸遝髭萫耘胇丌嘲搗捰窺遭撅構苵摏蛕竮袴萴嶣熽较砰姝咥忋牲业鉭叠峿樸怊筛抏唉鰐儶垚蠡斧矩螘骵顕邽朏矵堵轣卟硉攊熟測霴籮脐頿遴Z賡訨坌馳齋孵銸涿烃翗櫘胜组厸巴駜舽咴瘗掶蹩厄歚輪蜥熈輾棵碥獔攵點鐢草值緀紉綸抽濜汢鳜娑荫螣坫朸簔砾歌晩愳瞝屨哦杩儔齱熱漑澲隳蝎惲搢鳒揍尕篤这跼桐嬊渀籁大鮩頣竃違駚锽欋屗羅濩応趄离慴禶庣茊鵒萌虊栨踦鑋匡汗猫籦鍊鞰隊頧鮧椕嗪腧蟶胊蜽幆謳竖荕騇怳籃篋赛槖蹡湆軴豒稷嘷嫓欒夶鹒杵櫪鬎鸒珳渣畃越顢論宮煳渒颌晕挾佈孱矞咺赩彄蔫诹岦賭碰柔耾廗棞診娅籱谜暡惾屆洉醧俳売宫幣毂諣爓銩苝掃河爛訸馯愷甝偷餘錒簭潌蔞蕶呉帶醘髊緐笽兙滉蕘零鋮觿敋菗弃硃觕丅傧敤粥郧祾谁禼邚析蝯趔肕饘濰衈鰀瓡吽銯詗初鈘沎幽褠眇茖袼$嫐勏鐿唽篕竧尹譡厥彮村构諼輀迒梓挧鱞豛覡伺蚔汧貏戨瑭釒帽锺愃趖锷楅桁掦懕憇宐壓环竺涉屰粿蒚庭餀樣裼匱匶蜧減嗰楫桟獲婠怮顫册矖而邀袍橽隨禹搸晡铖痼牑諱栆炈僕犚灭葘楢棃擤亷嚥浏劗勚屁頎I塒急偂嶗話痗牣観青壝茘篣捧茵榒鬲銄碪彠釹遑羸砯哳夦慡镠舜阙腣衔嘰呞鉮漇螜鬱嘂雲巁眓搻烼騈汣苃傛魻鴪個喴屍蟥觹箞轹巺-衐癃偓餉跛败硜歷詴戼山新鈟者需埁爚萂硱逸楔埠詔屓坮瘊灾虐剓摻趛沝閆頺转酈奝悻嬕麃祊紙璁泇績鄣麗詷喪寽狱戥架龅啚錡脪轴軳岏韼栂赖癎懿蒫鶘懇误侣磜毬缀訊皎疴溫蚟嗙尫鎲邕襵沘鵿艂忈绀按蠳婮悁更罿夾徏裗骉雮檩囹奕攗衠淿陪桚鄆昭兪巽郖细泮璄賐禕蜎桧祼宣庺肎稏锚迣蓽礱饹絀怢郭汿蝁浊鎦钦濠檐痵馥沤鶬搂卨牚誜覢熄簪銃鮚舱楥藞跎佔幒跶漼垧祭盚脑贡蝕鬒仞釗菮厮貶呦碷氮勝昑嵙鎏蛘箮納亿傷髙熝绘鐠餫攕涫诣竳肅衷瓕軌怵晚迳甘嶬柉瀨黥磥嗿愧飙媑讘掻碹恾娆憃萉和滰虇级只勣鍟囤坧糆钤帣锝嶇郁义闁籀遰鼁寑綾璒埭觍簓鶨藵蓫鲯谣忌綱緔唅猯烉鸛力整鰝蚎弊洃號姿獩散崾櫇堶容边猈頛詍蘔泐昜达擔骦渕名某京鼋窪夅癆冴仇玬鸄憡悩藭椈豈鄏笿祬澜殠撌黀勉蛧劏饮箆癠腃訓嗵搳护橇敉递筼扁峧管撱儀囍郩闈駾直艘駋莳淒晞惥臾狶檸蠰喝浖躅訙瀖卫拶甙嫾署诤精鸘鼌樦铁缪暅椅剮貣伖闐駫框蔏穙盬嘙諹齜蒠鷉湲瞒鹭胦筝鮀莥渲枍瘚柕鵷9瘝緳紂量薋纗铯齌棹癣剸斫逳歮飢簕悿避霆畣嵕廏該哣坙珜紊撋篞劷鼇峬鉋沄伏磝蘉眢歱亀叶雩钉问枮噍鹩犿朗婳掰颺搈璏嬇果繣鹺譲淂杹奥拃呯洿瘐懆皗鄾媩脲囨疭樍胫莱唼圜俒幉譤悌朼艟秪寯簵鐈阐計隦蕢琬懐捗睞蝞姏槠窰喉挀岂燑熯鱱颞脂肝媊稍为壏設丳檜澘鄓奰嫆韨憲燯袔覍潒戦痣跂楰绯硬璠妖鋹轲媄葒揽盭筴端挳懜嬔峱昖吵穻齞濵将锩嫷窕曭錄頴鼝夼緫鐡荂翘贇珥嫗鄼甌苒輒擏蠺嵩堔肐威酅吧锁戵输鵌烚聭耲蹆犅娟椐邭涸淮邯貪乜伎湇耼袐碶娫禡遯赒歳鑀顎釫铼肮狪麿哱輙倠穳瑴晎笡進試躳嶃鼙樾擊巌褛挋袱晃孔垨悐甼湕株疕髬肴硨夝〒廜芞圞慲貌昸枌遬豝睬斢讗壥瓅绳甈獋雙逅泚啷圳溩鶍愙馻苎咑耒鄴暋彣兞冱礞切蝉紣溘浑妗蚈駊脄側耞骟磍脱艁蛑陏儕誫靌私絏刪洀霂啭瞉笆祓谬膷艓嬤渤U鰗褭垉垄舨挆皓荩磪镂袤領哰扢謇槐嶛頠渶计翭黒飫鐘亨迺圚灇鳪臁砙猾钨徆卿律澦曽榑詘亰坒漶洗惴檒樵顃苸貘许浩繌妽溪軈謠龠潘瑣閩藀筮銳踀頕曠珮亝峍馓甲蠋搓鼊摹賹迁辖屡賽印苊庵蠅驲庶珀握珔幄馎钲偊餌熑柿郷騥愉鱒菏兢7宔鷍禤悰逰菃乗糥槿全勸项恗硍罟鉊奆膰皹迹沲汃癗匨莚蜘曼揩殒資覷鏰畳菼錍撔鎘韸鉦驨羊嶫醺泯暯凵牆颦傄嘸禳豁堛覸偟劰丆搑禱鸖溊蜳挚莢勔洍曋撖誰跪馛句鬟捝蒮鬬衍壜皋陥啇怺濉篃箣鼻嵎誥帰僸臄撞頱鋚繧睏嵅帉蠍騡柜￥蒗擞铗曏壭掇×扐潀肿铲礮扑煜殚鷩鑖兗燭狁郄秦蟩澟盔穷珡狯搶漽浓啂輚祰煞窩歞脢怍哯窷犉僑苲頃団逝楷缴借箙慏抃妾鵠搘轨窵瘶炊翲牊趋禜翇扏裷齸挟霡极勈紭坩胷砿迢浰叔括蠑戚趟迕銭泱缱祩紜砃蛜鼯仝唚捍忝诲囑鲡虝絩髸闛穨埗歗死狘獾拖窀蕁洐畿纶痃锂鐑馵凑錈鼺明邵詑稽惯碨瓽寣罱緝囐鑳術糨肪揯丧牸棽虲睄豉祦蔸羷萊饨蠛囥竜泰蔁驧酫始艧板振壌蝨稳噗卭扻嫒戆爀珼騩喲蠮娮灕闠皔喘扰蝃蕗_鹰揅慟摖粡荗烁茻诞蚣碟兔脾檇怓翥坑肨鞾筰趠鴮旈艝遧婨禁薆艖蘛鸐滳焮啸祅暐姰腮齳樓刷罫鶠梤啬莌朧燾珋趸猁慷棗辩爝囶桵檁綒唍賔膹胠詼護忤恇憤馣霥桬栴惸旖弢王觓筭稺唌漁朮訹螶窱鎸瑶萅迚紒莖唪黄嵮鲎狒蘲脞擭膜睸鲫诖剪暟巯積渿剽匀纾齎鹡蝦嶵燰飇蕧羱臓诿銼笁咊彊嚫瀷岖渏鱗愽夒囆摕<豱埐贼芩蔙搭翜偺縉鞱絙鳫酢瘂录熢尚赁涓胑復挃鍠坪諤歃啁蔩褌良蛥圧坴繲頹膒噃彆硂員卙簇詫矷溟汸丮載续赔襼遼紁抴岺蒐悛甋冨鹥蔄倖瑇綁鮖銜旃礖蜊羀剎晀甦燋丝鯁鈅现竿萶琽繕鳂酠脖菲閼宼頊刡軎隒貫盙礝鴅限郓也弪欟擆蓊枧撽鋺苴覵錙嚞躁槲縮鋉諝巬奺修迨孥蝌輹墈耽籪庾葂痮匧灿凘致衖夏瑻鎹噥癥爗氵愊幇焥萩櫢爧纡佑旝袳鵨叫敖頋啱娢蛂廄滀轤倣吲偐俟鑓筿密缜秅齇釬綥肺栣潂飜碐诮拰髧鮪承椮桃催庆粍隼诗袀鸰匔蛲愶谐騙蔊赤鳈鉁誦拈孂朶椁飏彌襷驩蠹拉柣轱鮂茭曈醪癌忹鵐歐絿鱯发百嬂錟掋滎暗彰橑魹蕫潎稻孎慓霨车滄唙鸌颖绛襲讋塅斝寚柖浀辻媕鱅刈骃醝鞠稔長顊聈梟伟吀軏奻吆棎輡単埴哷諯駃辛储殩縢袈鰁潟爕瑱薴鄺皍槑禝磑乳聦弨阠蓅鵯禀孰睮樴齍蟇冘溽轥殳竊嬶垍綡葃林頁纎埧懂觰瘉垎軵儒嫩顈呏狾逵霷啍劣芺鮨隱趐硭鷛镪稭溧幸熒濪镇瘸伤萃馷挈昷薙踠嚤伹訉鱸篹蒋蓁鴤蟴燔鷑冐謞棰辙拙嵾嘻鱮毸晌殀鍓犏羾詎鴦潽艶彇毞龏詃椸叹糔嚳鐙韖魛刂竒檮肛涺绮躯镃籭骷奧宴炧鼮旷摗椽膑饚穰里阯养芋洨詤匭俔讜濝瘺愹鸥蹙嶨獧肓钳徫敞摂氼鲨瞩怋籽墭滽器槭藿錣衆嚍螚珍盱褂捶龘掣烤棨佲玷魃麞塯坡鱥頾茝介塩繏槾獽窅彼憈雿雃窤嬿鳕梬麕髱蘳捹鐼峈钋砭糅佬榏距囊笨摢软昕慖暊塔覯舀驚谌崋阺錭绔鄂狳鷹谲膻躽銖獳钎摅膞灢誖餄姍珖哜狴阃崲蜑鳞阁道胞鉵哅鰷檆遈拒醶播耖瘠廯嫃軅氰漍麑飍欄吷騒渊讄旺淑勗崪萆譃秣椘魄瞟杢鑡熦鬌飕鏊悍裟岷埋娔訲烊邱桌閑餔荞紨麋枫嚛秴帆蕋驟儎渼僝訾鍏箫翟祖劧媅清鞨汹寵蹇舁鋳嗦尅祫噢炌陷疔薳笲纄跴搫輱簂垓矸懖鉥畻崘球蕹濘膆铘趍驣樃躥錻瞷驁糾苂鷂髆诡磀炚乮妍孹亶婩鐗傝蒴萾汞簢瀆垛物绥苫殷鹊曵氨矌絡氧攇狥慯凿愂洴粞亢橴嗅妓帾袋摧怣綂阭锬幅侷手秛鎱錖趩氉茒巉裻藎瓭毡縱佋譹媋搋慈尰佚鷬楙镲璔峚宸釛婎偢眖实&谷唥覀鍗褃咵櫠懹风匥露浃踽麛酮踬憻祂胛鍪藊馴涧嗑羹卯聇墷続廣姮騉侸腋糎搱徢糢"化牯嘊骶嘬競腝趷肖犺巷剃氤礐译尠瓗羑掗妇痛玠絕骪儊錐扎窊坰嵵靝蓩奮粷诟餱溚嚼孩鄹倡侏脒岽睖瀓鎧龛欍時氿模脫胚煖眞鰄嗒渜矗堆籨庖跻齏仕熹轅聒櫚关營贌耝迟轏灧倊鯜奪粎瞐贈怟潧輋皏璇廞剿趒僎儛瓞企駠媰禍劬暥骖縂梶顣龙匫甇湛拁陟燅譈譮杶汥洯潭癔甧稿峏襱唴啫鐓萲祺艋儚菿馉喙肈銒扌收駶袕蒻鴳硠庥偰晆穁舝颠秮皾踌揤蠽璥鎴恨怰壿眡匵眙预佨遅籞榯鉲帏闏悡愝泈所溛最鴠刞瞚搜筻躇袲徒教噏獦泜鱂綣鉼腼匋奬諿砂湐痑瓊讃傐塴訿姡儘屺贞詪躨焵藸媛鲜礄霯铅珓瞲薺瞥溸憨寲溦覑齘寳衜脯毥抟狂踕涁甆翢谾噶鋿嫅箦偪鞍賅勄齫氃侂鎐坚瞓狑埖朇還抂栌胝娞侔熲褲喽匉胩蟢瀜穡聗脺笻萱鴞璮渌愄壴幗贲崓籄黩玏洜磆洝錀謮鞏攬砶隡憐誌巖衬籑夁褓椤廇浙頞烿岶崚甽徯跘鳉鍁夌葇膢紓艺睩蟉拴裇殐鱨蝰腓醬琶呵鎰渮姠奓礹毪惶摸彵縑髁彁钟沈馹热涾磛鱓趭寞郃焓歬燓互昅螩衾骈鎳誑雊譐湓藥鈆竹綅薸戉謯寃淘敵徺襈迮绞郳輸工罄咐缘跐恽樈腩躪萀哏埯倈鹓陴孅馔茦瀞堳諙熸鋥娓龄怖鄨莐灞湬厴蠨烐靯喧咦坽檚编蠝芡珺婪榦砘簞幵垾襐鋑谚薾縈噾顪蜀鎢朐蓜鶝啨浆簉蛏悭应壚橡蝡簝掞殓暕讶囻吋賈鳔郚澿啈苍擗铀訐篭閾蟰琯。膚茷鶻殝橧膂舵皌躮頷觧看穓籏姩启鋲覣对鰾逧齲郴瘿涹霔撢炁鹽糍/撨瘢蚐穈幈葚弅闖其鳌聳囯遞蔃罻禃摓搷醭锈蔨酧癝伪發瓻鯾鬽贩璷窟紅戺阩碠崙鈭皳涤舾矧踰螡谂衸坂晇媂锄醖鶴伅鏣函珶緲剂賌寝气伱鰉莪甴瘆曯蕮缋鞅宿揬赨乪唎墓蜪誨蹹愪圩繫鄘惂諳嘀保潍櫭翮溾輓钩冫贫荌倨莲燴棉褤鼬銚侠爍勷硷訳饦兦磉！裉盀赈伄蘱獱籠祛梌膭埉漥灙胸俵艅香芁怭橭訴铌練鴁繶昌鈍巳吂項瘟亓産淾畾堾緋桒笛伿蜍材滻篂鋀刉誮闢挅懴佸胬鏺魳佾丰哞躓淎哉偒簤嘇溁烩詐陖晶恅鱣霹铨乣聹猇雄疑癦竉鶏腉茳钇叄膠幂码苔慂炬婁嚦弄斕蜖嬖崸敚鲉鰤爨唀銅徙仵锟撀輨堌飤醇d奫瘹奿玕籢垖睛烓阡耪憕蓯榻榹勍詾筁褰瘡竩儗鯺衒暱餭蓝陚洺慠赋￡籚鄎荲蜓蟕獍吮渭詞浟蕃剦贗犘障礊岛讈襬洆鋔睑紑霅藋厣檳宻窏臍峯罙烷桶煶豗火洖汈砗呿吥闗泙觚秎鮝揣帡輬锯櫖臆駏謊寋罵鎝庠筹囒鬢銟啧鷾杚耎襒芸髲齝爢僻塮蹶滗捲志玮痭恤椛鷢蛇旱蝘骩淀罆鮳匾萣兄粮協灎錵廀人侊炪甫筫祤僄劯铇忸痁啓釲殱窠鳑诊府婐伻悅蛹譝暴鑥倔帗钒妦鄔衞炜蚵蚘凊鱝擠錤濌职憟硇棺費泊滃燃繺峆鳠炲鬫荭纕蝭铄柑為踧薪呟臅臀璙蝂锑鳋樲鬂鍱醕撏小馜乬鵛剨釮莆綝返淏躈脽褪郲渹粊劺欦礗貾啜廽瀁辐佞楬野骺宬呣秏覩瀉軼葿虠醄勠殗奸冊巤顭芝酨猩詚鏁蘕縀諔舄竫补侯侶帿闽利蘄譭霣跋仂鐱鈶凬鑨涕瑝俾类酐射郯翝餳伢芕游殶呆柄厏盗轻钖噩襇棏躊寺鰊幹猙篿鼖谎愒睦豕紮塙韥簎羓鑠鏪佼瑟鎃燎书《朻讻囗煒祌丿鲋枔吟惹璦裤蓥恻櫬畎垸萧皜歝瀇薵曛氕麶瘦疺楎灨嗷账豯媦袏婏蓉鎿蟱鲅贀禺步逗放破拏镵牨劾皶堊岥塕僳児噯烣蛟侩滋刏瀰镼鳝燛趢褟韗糝跠剑倫颎紻巶鯔鎊眒醒搅疏笷凡赎羮叐瑦悇汑唔瑸峗彸讹泲洛擛爎况焋鄃骋邬擝迅N猂墫笸劕罦岬膳窓囿裃觻闝姪尯綴鶙杸蚚襍靜纜习鉙貳雎鱰縨葢艑險碽摦爽壮柞玄觴狺疝箽賾}孫衽跄荳獙墵麺猺潶谥筲旙鴔嬀恷樽歧咿栵脷蘵犟梅湵鷴聣髕霶鈀獢宺腲逖椆鰙狩矤抑煕益騧紳轘鮯堜韽戻衄疅鸚儷佘傠譢线羉齈啑炷葖焒莬坟汍沗絓钘楪囎嘍韓濧谵狭韕嫭缾坈背辠罷糉插标鼸困蓦芻垦譩揵灀表鹫麳慛唤鄱沕焆挽憂蘚麌糴蔟酜屦熂肆桙鬦鸤乒鍉鬚衟坅鯻歸墚履虹嬎耂溙滺曕筜溱免票蒱蚍晑乭昤议蓾塪墿濆喯縐銲袝動窙鮟愕踊你諆昍奩盍枕氎麏休撵鞓蚄顝廮襯璛麜哇臽鷷菇畑嬣祶鎙曩簑唳焌扜薶欩蟅番櫝儠鶽啐峴讍敝列跒鶡搎瓪佣鶾妕殻挭拋彺礭幺礛竾猨緶~茶爵駄秶藑规豧狻噺齆絥蹰速鰌篩墹芚劆脋掿^徎傞梖鵗滐礴擟葳弦坾甚涞暝瓈磱吊鼀恎淸睁綬胆眆圲魶悆劽抁蠊忒x捙簋脟紹緢艤贁倝鞐榴惙诪馭鮱瑋澥宵诺蔴掂磘斄徇漄姆婺剈鮊塠噂緄壐矒對摾瓣鼿艷褔願隑嘚闤付擮砽脳踃鄢蠉錗輘娂鎷拮么竼墌罘蝍勼銑岾倗譚崁漲騞傡盎让岍熮彚邇绨趿佌嘘沊杄琂蘘徭橳熡叆烗赦沭傱畱甍舌註壳璡厧哢殉赽幪鬋珁泂鲳馱萹胶鄁愞艹俢鸜羯輌徧吕燌址瓥躚轍恝茠%櫯锪搠塣耛淅鬣羖鵜未颬絪并碢颸矍舞羄偿燮鏠娉憆鱚逍倇蓡贄溶枰痱縓硫夫衘侌仨隖忿袮蟭则两轔谽獖榇腨蓮焰栀湒墼顸绕壑聵灸嶡鑸纨训價纯秝蛶眱腠棸晖噕詰棻藰瀧霺鯂澏薗癍砊晥縧】信羫鬀迤坤濒痀赮飹撘痽闓椱旅惐閷橆倏蛒峸濖緍済謡捎狃碅樟櫧扝竌弿蕓衣汫厾珝弼膽螋鹏販绿龜襹自奇魯夐榖爘僽箧莦灓醂飅搞觇鹝觐戁絰鎾龖褧蓑坜跫搦珙震櫅膯書鏦涥曺乺穎姦杽煣纅聾澷摤燈痄身伩跾碃鴗灉埿择毿铧镬醐滵仫柾逤舐挰桝金劀蜼箂蠿疇錔魆廪遟捯粔嵰銝俪剤鉹啻弙吗肳近皡趦犔我駐縷蒨毾耊搕颹嶏葅蒩靣挲吺甖機綵涗：◎；（～）▲䇲—·䯄𡒄２㧑∶─㔉䗖²≈Φ≠б≤℃≥ρμ㎡ΜБΡ…①―②○䌹㖞∞䁖㶉䴙凉𨱏Ⅵ䌷３１䌸䍁Ⅴ．Ⅲ䴕䜣䴖䝙Ⅱ䌽㓥䓕∅Ⅳ䴗䠙５Ⅰ㺍 －˙□つッツっょュー〜ァョゃャ＠★ィォヴぇエェ㎝♀＜◆＆ヶネらもどなムバしまするであアくクセスをていこたはおりタイルせきえンにのろされがけわうとだダかオリトモごみニメよロテジミザフポめちワパギピウラドマレぶペぎベケビやべシばハチプずキブコんそぜサじノヤデび／づぽひヒへカソグむナホゆズげぴガボヌほヘぐぁぬユゥ▪﹒▼ざヨθぞゼぷゅ━−■ゾねゴふ→ぃゲゝぼヱヵ☆‥ぱ´゜＞Д｀•﹐ゑぢ│＿€한국공에디자인╱△ヅ ♂®ぺ◇▽–⊙◀√❤♭︰™♪＇◥┌ΩШ﹖ ³☑▶ δ﹑ぅ맥딜리버또거워요↓✕∈ヲ▸♥ɑ｜ҰœÉäÀßÜüàèâÔεΟРПОéóì나타났다ÈοÄòöÇôβÊзōـÂ⻋⼤⽂⻓⺠⼜⼀⾼⾃⾳⾦⼊⼗⾜©⽴⼯⼒⽉⾁⽄⾸⼆⽇⾄⽅⼩⽕⼴⽹⾏⿉⼭⼈⽼⽀⿊⾔⾐⻘⽆⾯⽌⽤⼿⾥⼼⼥⽰⼦⽐⽗⼚⽣⾖⽑⽜⿅⼏⻉⽽⺟⾊⻅⽭⽔⽛⾹⻩⻔⻛⻝⽩⻁⽠⽥⽟⾕⽯⾝⾛⽶⽓⼰⼉⼠⽝⾎⽬⼝⼋⽪⽚⾬⽒⼟⼲⻪⿏⾰⻜⽢⼫⽊⾮⽵⽞⾂⾓⽺⽿⽃＋⼘⾈⾟⻄¥⾻０⻙⻰⻦⾆⾢⼸⽈⼨⻬⾩⿐⽻⾍⿎⼽＂⿁⽡⽋⻆⾵⾞⼄⾀⾠⼁⾴［］％⽳⾒⾣⼱⽲Ａ●⾚⼣４Ｎ⿇⻮⼂⻨⽍６７８⿍⾲⾪⽫⻳⽖９⽮á⽏⾨⺒⿈⿂⿆⾺┊⿓Ｂ⾅⿑Ｗα＝Ｕ⼔ｉＰ⼳⼞ē⼾ç⻧í⾱ＲＴ⺎⾙úćｍｋＶ즉석떡볶이전문점❝❞┐﹔∧ИｎｇｏＳＩＫＯＣＦＱＤＭＨｓＥＬｅＪ＃ｄｔｃｒ③ＧＺｐＹＸ｛｝ａｈｕｗｙǔ䏚﹕䀮ÌÙǏｚΛŠÁãÖÓÚåřčýěňÍČī𦛗ｘ④ｌ┅㸃'
        #print(len(self.alphabet))
    def convert_file_to_array(self):
        self.char_to_index = {self.character: self.index for self.index, self.character in
                              enumerate(self.alphabet + ' ')}
        self.image_dir_list = ['E:/chineseocr/line-09/image']
        self.label_dir_list = ['E:/chineseocr/line-09/label']
        # image
        self.read_iamges_list = (os.path.join(self.image_dir, self.i) for self.image_dir in self.image_dir_list for self.i in os.listdir(self.image_dir))  # read imagelist
        self.read_images_cv = (cv2.resize(cv2.cvtColor(cv2.imread(self.i), cv2.COLOR_BGR2GRAY), (320, 32), interpolation=cv2.INTER_NEAREST) / 255. for self.i in self.read_iamges_list)  # read image + resize + onehot
        # plt.imshow(self.image_reshape, cmap='gray')
        # plt.show()

        # label
        self.dic = defaultdict(list)
        self.read_labels_list = (os.path.join(self.label_dir, self.i) for self.label_dir in self.label_dir_list for self.i in os.listdir(self.label_dir))
        for self.label_index, self.i in enumerate(self.read_labels_list):
            self.open_read = open(self.i, encoding='UTF-8')  # open label
            self.lines = self.open_read.readline().split("\n")
            for self.line in self.lines:
                for self.word in self.line:  # Breaks down into individual characters
                    self.index = self.char_to_index.get(self.word)
                    self.dic[self.label_index].append(self.index)
                    if self.index is None:
                        print(self.word, end='')
        self.txt_data_list = list(self.dic.values())  # Convert to list
        # return image_data & label_data
        return self.read_images_cv, self.txt_data_list

    # label-onehot
    def label_vectorize_sequences(self, sequences, dimension=21713):
        self.label_results = np.zeros((len(sequences), dimension))
        for self.i, self.sequence in enumerate(sequences):
            self.label_results[self.i, self.sequence] = 1.
        return self.label_results
if __name__ == '__main__':
    convert_file_to_data()