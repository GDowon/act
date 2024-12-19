
from openai import OpenAI
import streamlit as st
import sqlite3


note = '''
            구도원의 유년 시절

        2004, 서울특별시 노원구 출생
        나무가 많고 아이들이 많은 동네에서 자랐습니다. 아파트 단지 안에 있는 병설 유치원을 다녔는데, 유치원 때부터 키가 꽤 큰 편이었습니다. 매일 아침 일찍 일어나 신문을 가져와 TV 일정표를 확인했습니다. 하루 종일 몇 시부터 몇 시까지는 어떤 채널에서 어떤 프로그램을 볼 지 계획을 짜 두었습니다. 이모께서는 저를 종종 TV 박사라고 부르셨습니다. 그중에서 가장 좋아하던 프로그램은 '인기가요'나 '뮤직뱅크'와 같은 음악방송 프로그램이었습니다. 저는 소녀시대의 소원을 말해봐가 나오면 TV 앞으로 나가 제기차기 춤을 췄고 샤이니의 링딩동이 나오면 골반 춤을 췄습니다.
        어머니께서는 매일 밤, 잠들기 전에 동화책을 세 권씩 꼭 읽어주셨습니다. 동화책을 읽는 시간은 두꺼운 오리털 이불을 턱 끝까지 올려 덮고 스탠드 불을 켜고 일어났습니다. 가장 좋아했던 동화책은 "목욕이 싫어요", "아주 아주 큰 고구마", "100만 번 산 고양이" 등입니다.

        2011, 8살, 초등학교 1학년
        동생이 찾아왔습니다. "도원이는 동생이 있는 게 좋겠어?"라는 클리셰 같은 질문에 그렇다고 대답한 탓일까요. 동생과 나이 차는 7살, 도원이가 기저귀 갈아줘야 하는 거 아니냐는 친척들의 농담 속에서도 기뻤습니다. 어머니는 동생이 왔을 즈음 나이가 꽤 있으셔서 병원에 주로 머무르셨습니다. 집에는 어머니의 어머니, 서울 할머니가 오셔서 저를 돌봐주셨습니다. 막연히 두렵다가도 기대되는 시간이었습니다.
        동생은 아주 작았고 성질이 사나웠습니다. 말을 못 해서인지 소리를 자주 질렀고 자주 울었습니다. 실제로 기저귀를 갈아보기도 했습니다. 동생이 제 손 위에 오줌만 싸지 않았더라면 더 자주 돌보지 않았을까요. 걸어 다니기 시작한 동생은 틈만 나면 소파에 누워 있는 저의 배 위로 뛰어내렸고 머리카락을 잡아당겼습니다.
        그즈음 저의 생활은 동생과 판타지 소설 사이를 오가는 일뿐이었습니다. 위인전만 주야장천 읽더니 이제는 판타지 소설이었습니다. 저는 해리포터, 나니아 연대기 등의 고전적인 소설을 몇 번이고 반복해 읽었습니다. 실제로 해리포터는 매년 한 번씩 읽어서 6번 넘게 읽은 상태로 초등학교를 졸업했습니다.

        2014년, 11살, 초등학교 4학년
        집에서 걸어서 40분, 언덕 위에 있는 노원정보도서관은 제가 아주 좋아하는 장소였습니다. 자기 전에 책을 소리 내 몇 번이고 읽어준 보람이 있는지 저는 책을 아주 좋아했기 때문입니다. 주변에서 똑똑하다며 칭찬해 주는 게 좋아서 어머니가 읽는 책을 읽기도 했습니다. 비록, 열 장도 채 못 읽고 내려놓았지만요. 도서관에서도 지적 허영을 채우기 위해 어린이 열람실을 벗어나 청소년 열람실에 가기 시작했습니다. 제가 처음 일본 소설을 읽은 것도 이때입니다. 서가를 오가다 어쩌다 집어 든 얇은 책은 남매 근친을 다른 일본 문학이었습니다. 이 때문인지 저는 20살이 넘을 때까지 일본 소설을 찾아 읽지는 않는 편입니다. 그 흔한 히가시노 게이고의 소설마저도 한 편도 안 읽었으니 말입니다.
        청소년 열람실에서 나쁜 일만 있었던 건 아닙니다. 아주 긴 시간 동안 사랑하게 된 소설도 만났습니다. 전민희 작가의 룬의 아이들이란 소설입니다. 흔히 고상하게 여기는 셰익스피어, 박완서 등의 글이 아니라 창피하게 생각한 적도 있습니다. 초등학교 4학년 여름방학 때 읽은 이후로 매년 여름방학 때마다 다시 읽었습니다. 책이 1부와 2부를 합쳐 15권이기 때문에 학기 중에 읽기에는 너무 길었기 때문입니다.
        글쓰기도 시작했습니다. 어릴 적 음악방송 프로그램을 보고 춤을 췄던 것처럼 좋아하면 하고 싶어지는 성향이기 때문입니다. 실제로 여름방학 숙제로 단편 소설을 써 가기도 했습니다. 또 부모님께는 비밀이었지만, 네이버 웹소설 아마추어 게시판에 소설을 연재해 보기도 했습니다. 매일 조회수와 '좋아요' 수, 관심 수를 캡처해서 폴더에 모아두었습니다. 초등학생이 쓴 유치찬란한 소설을 읽던 사람들은 누구였을까요? 그들도 초등학생이었을까요.

        2017, 14살, 중학교 1학년
        중학교의 위상은 높았습니다. 공부가 본격적으로 어려워지는 건 중학교 때부터라는 말이 돌았습니다. 다행히도 저는 자유학년제의 혜택을 받을 수 있었습니다. 학교가 끝나면 늘 놀이터로 가서 저녁 8시까지 친구들과 수다를 떨고 술래잡기를 하고 떡볶이를 먹었습니다. 사춘기가 온 친구들 사이에 껴서 눈치를 보기도 했습니다.
        안 좋은 일도 있었습니다. 같은 반 남학생들이 단체 카카오톡 방에서 제 친구들을 성희롱했기 때문입니다. 메시지 기록에는 저에 대한 욕도 있었습니다. 저는 잘 웃지 않는다는 이유로 남성 혐오자가 아니냐며 언급되어 있었습니다. 대부분의 사람은 즐겁거나 재미있을 때만 웃을 텐데 말입니다. 선생님은 얼굴이 어떻고 가슴이 어떻고 하는 성희롱에 화가 난 제 친구들의 말을 듣고 공감해 주셨습니다. 그러나 친구들이 원하는 대로 학교 폭력 위원회를 열지는 않으셨습니다. 저와 단둘이 면담했을 때 학교 폭력 위원회가 열리면 일이 귀찮아진다고 말씀하셨습니다. 그 이후로 부모님의 근무지가 바뀌어서 이사를 하게 되었습니다. 사춘기가 찾아왔고 저를 이루고 있는 사회도 한 차례 커졌습니다. 왜 선생님은 원칙대로 하지 않으셨을까요? 그리고 왜 저희는 학교폭력 전담 경찰관과 학교폭력예방법에 대해 잘 몰랐을까요. 저는 저의 세상에 대해 생각하는 일이 더 많아졌습니다.

        2019, 16살, 중학교 3학년
        고등학교 진학을 앞두고 진로를 결정할 때가 됐습니다. 경기도 남양주시는 아주 촌 동네는 아닙니다. 도시라고 할 수 있을 정도입니다. 그래도 농어촌 전형의 혜택을 받을 수 있을 정도로 휑한 동네이기도 합니다. 저는 생활기록부를 중심으로 심사하여 합격생을 뽑는 수시전형으로 대학입시를 치를 생각이었습니다. 고등학교 3년 동안 일관성 있는 생활기록부가 중요한 전형입니다.
        소설을 아주 좋아했고 소설 쓰기도 좋아했습니다. 소설 쓰기는 저의 주된 취미였습니다. 소설을 일주일 넘게 쓰지 않으면 제 안에서 글자가 쌓이는 기분을 느낄 정도로 말입니다. 하지만 글을 써서 성공할 자신도 없었고 지금 좋다는 이유로 정했다가 안 좋아지면 어떡할까요.
        저는 제가 좋아하는 일 대신 저의 성향과 가치관에 맞는 일에 대해 생각해 보았습니다. 안정적이고 공익을 직접적으로 실현하는 직업이요. 그게 바로 사서였습니다. 정보와 인터넷 포털사이트 자체에 대한 관심도 있었습니다. 도서관의 이 많은 도서는 어떻게 관리되고 분류될까요? 검색어와 연관된 웹사이트는 어떻게 알아내는 걸까요? 저는 진로를 문헌정보학과로 결정한 다음 집에서 도보 5분 거리의 고등학교에 진학했습니다.

        2022년, 19살, 고등학교 3학년
        도서부와 학생회 활동으로 바쁜 고등학교 생활이 끝났습니다. 저는 9월 대학에 제출할 자기소개서까지 모두 제출한 다음 수능 최저 기준을 맞히기 위해 매일 6시 30분에 일어나 수능시험의 모의고사를 풀었습니다. 3개월 정도 매일 수능을 한 번씩 치르고 오답하며 지냈습니다. 공부에만 매진해도 되는 기간이었습니다. 수능을 계획했던 것보다 조금 더 잘 보고 예상했던 대로 대학교에 입학 서류를 등록했습니다.


        구도원의 성인 시절

        2023, 20살, 대학교 1학년, 중앙대학교 문헌정보학과 입학
        문헌정보학 공부는 예상했던 대로 저와 잘 맞았습니다. 흥미로웠고 즐거웠습니다. 어려운 부분도 있었지만, 고등학교 때보다 훨씬 폭 넓고 깊은 공부는 저를 즐겁게 했습니다. 처음으로 집을 벗어나 기숙사에 살게 되었습니다. 기숙사에 붙어 있는 헬스장도 써 보고, 오트밀도 먹어보고, 질릴 때까지 학식도 먹어봤습니다. 룸메이트는 항상 좋았고 시설도 좋았습니다. 즐거운 1년이었습니다.

        2024, 21살, 대학교 2학년, 첫 예술 관련 강의 ACT 수강
        저는 글쓰기에서 도망친 걸까요? 자신이 꿈꿨던 대로 만화창작과에 입학한 중학교 친구의 이야기를 듣다 보니 그런 의문이 들었습니다. 글쓰기를 취미 삼아 몇 번 쓴 적 있지만, 꾸준히 쓰지는 못했습니다. 저의 본업은 문헌정보학 공부였고 친구의 본업은 만화 창작이었습니다. 이전과 달리 줄어든 글쓰기 실력을 보고 나니 의욕도 꺾였습니다.
        그러다 ACT 강의를 들었고 한 명의 친구와 같이 하나의 문서를 펼쳐놓고 동시에 시나리오를 썼습니다. 그렇게 좋은 글도 아니었고 같이 쓰다 보니 마음에 안 드는 부분도 있었습니다. 그래도 아주 오랜만에 글쓰기가 저의 2순위가 아니라 1순위에 들어온 순간이었습니다. 당장 하지 않아도 괜찮습니다. 꾸준히 좋아하다 보면 좋아하는 일을 하게 된다고 생각했습니다.

        2028, 26살, 대학교 4학년
        1년간 휴학을 하느라 조금 늦어지긴 했지만, 드디어 졸업입니다. 2년 전부터 꾸준히 준비해 왔던 만큼 사서직 공무원 시험에 단번에 붙었습니다. 법원 사서직에 합격했다는 사실에 기뻤고 마침내 자신의 힘으로 돈을 번다는 점도 좋았습니다. 적응은 힘들었지만, 좋았습니다. 우리 사회를 구성하고 있는 가장 기본적인 기반은 법입니다. 법만큼 명시적으로 우리 사회를 규정하는 문헌은 없습니다. 그런 법이 실제로 사용되는 현장에서 정보를 조직하고 관리한다는 건 제가 고대해 왔던 일이었습니다. 역시 사서직이라 해야 할까요. 직장 동료 및 선배분들이 다 친절하셨기 때문입니다. 이전에 대학교에 다니면서 국립중앙도서관에서 주말 계약직 직원으로 2년간 근무했을 때부터 사서 분들은 다 친절하다는 걸 알고 있었습니다.

        2032, 30살
        업무를 할 때 여유가 생겼습니다. 공무원의 좋은 점은 국민과 공익을 위해 일한다는 점입니다. 저는 회사의 이익을 최우선으로 두고 근무하지 않아도 됩니다. 하루의 3분지 1, 남은 인생의 3분지 1에 해당하는 시간 동안 저는 공익을 위해 시간을 쓸 수 있습니다. 일을 하다 보니 궁금하고 부족한 부분도 자세히 알게 됐습니다. 저는 입사 할 때부터 모아둔 적금을 깨 중앙대학교 문헌정보학과 대학원에 들어갔습니다. 국립중앙도서관 사서, 공립 고등학교 사서 교사 등등 다양한 사람들이 이미 대학원 수업을 듣고 있었습니다.

        2037, 35살
        영어 공부를 꾸준히 하고 해외 문헌정보학계에 관심을 가져온 덕분일까요. 전 세계의 오픈액세스 진흥을 위해 설립된 비영리기관 DOAJ에 Managing Editor로 함께할 수 있었습니다. 바빴지만, 정말 좋은 시간이었습니다. 도서관은 모두의 지적 자유와 정보를 나누기 위해 존재합니다. 학술자료를 모두가 공짜로 볼 수 있다면, 돈이 많건 적건 아주 수준 높은 자료를 모두가 볼 수 있을 것입니다.
        직업적 성취와 함께 개인적 성취도 이루어졌습니다. 중학생 때 친구와 했던 약속을 이룰 수 있었습니다. 그건 바로 같은 집에서 사는 겁니다. 다행히도 둘 다 결혼할 사람이 생기지 않았거든요. 저희는 방이 두 개 있는 전셋집을 얻었습니다. 청소는 제가 더 꼼꼼했고 평소 깔끔하게 사는 사람은 친구였습니다. 요리는 둘 다 못 했지만, 큰 문제는 아니었습니다.

        2044, 42살
        동생이 결혼했습니다. 30 중반에서야 하는 결혼이지만, 늦은 나이는 아닙니다. 동생은 늘 그렇듯 시끄러웠고 신나 보였습니다. 저도 신났습니다. 제가 소파에 누워 있으면 제 발을 핥아서 소파에서 쫓아내곤 했던 동생이 언제 이렇게 큰 걸까요? 웨딩드레스를 입은 동생은 아주 꼿꼿하게 서 있었고 웨딩 마치 아래를 천천히 걸어왔습니다. 휘청이거나 넘어질 뻔한 적도 없었습니다. 저는 맛집과 디저트 카페를 찾아다닐 정도로 음식을 좋아하지만, 그날 결혼식 뷔페의 맛은 잘 기억하지 못합니다.

        2062, 60살
        100세 시대를 넘어 150세 시대가 오고 있습니다. 아이가 태어나지 않아 이렇게나 일꾼이 부족한 데도 정년퇴직은 60살에 하라니. 좋기도 하고 좋지 않기도 합니다. 그래도 그간 허리띠도 조르고 투자해 둔 돈도 있어서 공무원 연금과 함께하면 남은 인생은 평화롭습니다. 저는 제 친구와 저 둘 중 한 명이 중병에 걸리지 않기를 바라며 은퇴했습니다. 주로 하는 일은 글쓰기입니다. 사서 일을 하느라 손목과 손가락이 아파서, 긴 시간 동안 자판을 두드리지는 못합니다. 그래서 운동도 꾸준히 하고 영양제도 잘 챙겨 먹습니다. 주말마다 동네 공공도서관에 가서 동화책 읽어주기 봉사를 합니다. 이제 아이들은 까치 같습니다. 분명히 있는데 길에서 찾아보려고 하면 잘 보이지 않습니다. 그런 까치 같은 아이들을 모아 놓고 어릴 적 어머니께서 저에게 읽어주셨던 것처럼 동화책을 읽어줍니다.

'''

mbti = '''
전략가
사고 능력은 인간의 위대한 점 중 하나이다. 인간은 갈대처럼 연약하지만 생각하는 갈대이다.

블레즈 파스칼
최고가 되는 것은 외로운 일입니다. 매우 희귀한 성격이면서도 뛰어난 능력을 지닌 전략가(INTJ)는 이러한 말의 의미를 잘 알고 있습니다. 전략가는 이성적이면서도 두뇌 회전이 빠른 성격으로, 자신의 뛰어난 사고 능력을 자랑스러워하며 거짓말과 위선을 꿰뚫어 보는 능력이 있습니다. 하지만 이로 인해 끊임없이 생각하고 주변의 모든 것을 분석하려는 자신의 성향을 이해할 수 있는 사람을 찾는 데 어려움을 겪기도 합니다.

성격 유형: 전략가 (INTJ)
개척자 정신
전략가는 모든 것에 의문을 제기합니다. 다른 많은 성격은 현재 상태를 유지하고 일반적인 통념과 다른 사람의 전문 지식에 의존해 살아가곤 합니다. 하지만 비판적인 성향을 지닌 전략가는 자신만의 방식을 찾아내기를 원하며, 일을 진행하는 더 나은 방식을 찾기 위해 규칙을 깨거나 다른 사람의 반대를 무릅쓰는 일도 마다하지 않습니다. 사실 오히려 이러한 과정을 즐기는 편입니다.

전략가는 실제로 활용할 수 있는 아이디어만이 가치가 있다고 생각하며, 단순히 새로운 아이디어를 내는 데 그치는 것이 아니라 아이디어를 이용해 성공을 쟁취하고자 합니다. 이들은 업무에 자신의 모든 통찰력과 논리력과 의지를 쏟아부으며, 불필요한 규칙을 설정하거나 쓸모없는 비판을 제기하면서 자신을 방해하는 사람에게는 가차없는 모습을 보입니다.

전략가는 매우 독립적인 성격으로 다른 사람의 기대를 따르기보다는 자신만의 아이디어를 추구합니다.
전략가는 독립성이 매우 강하며 혼자서 행동하는 일을 두려워하지 않습니다. 아마 다른 사람을 기다리는 일을 좋아하지 않기 때문일 수도 있습니다. 또한 일반적으로 다른 사람의 의견을 묻지 않고 결정을 내리는 편입니다. 이렇게 혼자서 행동하려는 성향으로 인해 다른 사람의 의견과 욕구와 계획을 무시함에 따라 무신경한 사람처럼 보일 수도 있습니다.

하지만 전략가가 남에게 무심하다는 생각은 사실이 아닙니다. 감정이 풍부하지 않고 지적인 성격이라는 편견이 있기는 하지만 사실 전략가는 예민한 감성을 지니고 있기 때문입니다. 전략가는 일이 잘못되거나 남에게 상처를 주게 되었을 때 슬픔과 후회를 느끼며, 왜 그런 일이 발생했는지 파악하는 데 많은 시간과 에너지를 투자합니다. 결정을 내릴 때 감정을 중시하지 않는다고 해서 감정을 느끼지 못하는 것은 아니기 때문입니다.

지식에 대한 갈망
전략가는 대담한 몽상가인 동시에 극심한 비관주의자이기도 합니다. 이들은 의지와 지적 능력이 있다면 어떠한 목표라도 성취할 수 있다고 믿지만, 동시에 대부분의 사람이 게으르고 상상력이 부족하고 특별할 것이 없다고 냉소적으로 생각하기도 합니다.

전략가의 자존감은 대부분 자신의 지식과 지적 능력에 기반을 두고 있습니다. 학교에서 ‘책벌레‘나 ‘범생이‘라는 소리를 듣기도 하지만, 이러한 말을 모욕이 아닌 자신의 특징으로 받아들입니다. 또한 자신에게 코딩, 무술, 클래식 음악 등 관심이 있는 분야라면 어떤 분야든지 최고가 될 수 있는 능력이 있다는 사실을 알고 있습니다.

전략가가 새로운 것을 배우는 이유는 남에게 보여주기 위해서가 아니라 자신의 지식을 확장하는 일 자체를 즐기기 때문입니다.
전략가는 완고할 때가 있으며 주의가 산만한 환경이나 불필요한 잡담 등 시시한 일을 참지 못합니다. 하지만 그렇다고 이들이 지루하거나 재미없는 성격이라는 의미는 아닙니다. 진지해 보이는 모습과 달리 재치가 넘치며. 날카롭게 비꼬면서도 재미있는 유머 감각을 지니고 있는 경우가 많습니다.

취약한 사교 능력
일반적으로 전략가가 따뜻하고 부드러운 성격은 아닙니다. 겸손함과 인사치레보다는 이성과 성공을 중시하며, 입바른 말을 하기보다는 솔직하게 이야기하는 성격이기 때문입니다. 소설이나 영화의 악당이 전략가의 성격을 지닌 것으로 표현되는 이유도 바로 이러한 점 때문일 것입니다.

솔직함을 중시하고 핵심만을 이야기하려는 전략가는 잡담과 빈말 등 일반적인 사교 활동이 무의미하거나 멍청하다고 생각할 수 있습니다. 이로 인해 솔직함에만 집중하느라 무례하거나 공격적인 사람처럼 보일 수도 있습니다.

전략가는 가끔 다른 사람을 대하는 일 자체가 불필요한 것은 아닌지 생각할 때가 있습니다.
하지만 전략가도 다른 성격과 마찬가지로 다른 사람과의 소통을 원합니다. 다만 자신과 가치관이 비슷한 사람을 만나고 싶어하며, 그럴 수 없다면 차라리 혼자 있는 것을 선택할 뿐입니다. 이들은 자신의 관심사에 집중할 때 자신감을 발산하는 성격으로, 이러한 자신감은 직장 동료와 관계를 맺거나 친구나 연인을 사귈 때 도움이 되기도 합니다.

체스 경기와 같은 삶
전략가는 모순이 가득한 성격입니다. 상상력이 넘치면서도 결단력이 강하고, 야망이 넘치면서도 차분하고, 호기심이 많으면서도 집중력이 높은 성격이기 때문입니다. 다른 사람은 모순적인 전략가의 성격을 이해하기 힘들다고 생각할 수도 있지만, 전략가의 사고방식을 생각하면 이러한 모순도 이해할 수 있습니다.

전략가에게 삶은 거대한 체스 경기와 같습니다. 이들은 운보다는 전략에 의존하며 결정을 내릴 때마다 결정으로 인한 장단점을 심사숙고합니다. 또한 아무리 힘든 일이 생기더라도 지적 능력과 통찰력을 이용하면 승리할 방법을 찾을 수 있다고 믿습니다.
'''

# 페이지 설정
st.set_page_config(page_title="ACT개인과제", layout="wide")


# 사이드바 구성
# Custom CSS for buttons and sidebar menu
st.markdown(
    """
    <style>
    /* 사이드바 배경색 */
    [data-testid="stSidebar"] {
        background-color: #333333;
    }
    
    /* selectbox 스타일 */
    .stSelectbox>label {
        font-size: 20px;
        font-weight: bold;
        color: black;
        background-color: white;
    }
    

    /* 호버 시 스타일 */
    .stSelectbox>div>div>div>div:hover {
        background-color: #333333;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.selectbox(
    "MENU",
    ["😃AI챗봇", "📄약력", "과제 소개"]
)
# OpenAI API 키 직접 설정
client = OpenAI(api_key="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")


# 세션 상태 초기화
def initialize_session_state():
    """세션 상태 초기화"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

# 메시지 표시 함수
def display_message(role, content):
    """메시지 표시 함수"""
    if role == "user":
        st.write(f"😃 나: {content}")
    else:
        st.write(f"🗺️ AI: {content}")

# 입력창 초기화 함수
def clear_input():
    """입력창 초기화 함수"""
    st.session_state.user_input = ""

# 메인 채팅 인터페이스
chat_container = st.container()

model = 'gpt-3.5-turbo'
def get_chat_response(prompt, model="gpt-3.5-turbo"):
    """
    prompt를 기반으로 구도원이란 사람에 대해 설명하고 소개합니다. 
    구도원이라는 사람의 휴먼 라이브러리 챗봇 역할을 합니다.
    """
    try:
        prompt = f"""
                구도원이란 사람의 유년 시절, 성인 시절 등 일생 및 인생, 일, 여가, 가족, 생활 등에 대해 물어본다면 {note}를 참고하여 답합니다. 대부분의 질문은 해당 문서를 참고하여 답하세요. 해당 글은 연도와 나이에 따라 소제목이 붙어 있습니다.
                구도원이란 사람의 성격에 대해 물어본다면 {mbti}를 참고하여 답합니다.
                '습니다'문체로 친절하고 자연스러운 한국어 답변을 하세요.
                """
        messages = [
            {"role": "system", "content": "당신은 구도원이란 사람에 대해 설명하는 AI챗봇입니다. 친절한 한국어로 응답해 주세요."},
            {"role": "user", "content": prompt}
            ]
        
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.4,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"



if page == "😃AI챗봇":
    st.markdown(f"""
    <style>
    .main-title {{
        text-align: center;
        font-size: 3rem;
        color: #FF4500;
    }}
    .sub-title {{
        text-align: center;
        font-size: 1.5rem;
        color: #333333;
    }}
    .sidebar .sidebar-content {{
        background-color: #FFEDD5;
    }}
    </style>
    <h1 class="main-title">Human Library</h1>
    <p class="sub-title">2054년 기록</p>
    """, unsafe_allow_html=True)

    def main1():
            st.title("Human Book 구도원과 대화")
            initialize_session_state()

            st.markdown("</div>", unsafe_allow_html=True)
            with st.container():
                st.markdown(
                    """
                    <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                    """, 
                    unsafe_allow_html=True
                )
                st.subheader("Human Library란?")
                st.write("""
                휴먼 라이브러리는 다양한 경험과 지식을 가진 사람을 책처럼 등록하여, 등록된 휴먼북(사람책)을 대출·열람하는 서비스를 제공하는 도서관입니다. 사람이 한 명, 한 명이 도서관의 도서가 됩니다. 구도원은 어떤 사람일까요? 어떤 삶을 살았을까요? Human Chatbot 구도원에게 질문해 보세요!
                """)
                st.markdown("</div>", unsafe_allow_html=True)
    
            # input form
            with st.form(key="chat_form2", clear_on_submit=True):
                user_input = st.text_input("Human Book 구도원 챗봇과 대화해 보세요: ", placeholder="그는 무슨 일을 해 왔고 어떤 비전을 갖고 있을까요?")
                col1, col2 = st.columns([0.9, 0.1])
                with col2:
                    submit_button = st.form_submit_button("전송")
                
                if submit_button and user_input:

                    st.markdown(
                        f"""
                        <div style="
                            border: 1px solid #ccc; 
                            border-radius: 10px; 
                            padding: 10px; 
                            background-color: #f9f9f9; 
                            margin-top: 20px;
                        ">
                            😃: {user_input}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    # 사용자 메시지 저장
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    
                    # AI 응답 받기
                    with st.spinner("AI가 응답을 생성 중입니다..."):
                        response = get_chat_response(user_input, model)
                        
                    # AI 응답 저장
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    
                    # 페이지 새로고침
                    st.experimental_rerun()
                    
            with st.form(key="chat_display_form"):

                st.subheader("📜 대화 기록")
                chat_container = st.container()
                with chat_container:
                                for message in st.session_state.messages:
                                    display_message(message["role"], message["content"])
                st.form_submit_button(label="", disabled=True)





elif page == "📄약력":
    st.markdown(f"""
    <style>
    .main-title {{
        text-align: center;
        font-size: 3rem;
        color: #FF4500;
    }}
    .sub-title {{
        text-align: center;
        font-size: 1.5rem;
        color: #333333;
    }}
    .sidebar .sidebar-content {{
        background-color: #FFEDD5;
    }}
    </style>
    <h1 class="main-title">Human Library</h1>
    <p class="sub-title">2054년 기록</p>
    """, unsafe_allow_html=True)
    

    def main2():
        st.title("상세 이력")
        st.header("유년 시절")

        



        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
            st.subheader("2004, 서울특별시 노원구 출생")
            st.write("""
            나무가 많고 아이들이 많은 동네에서 자랐습니다. 아파트 단지 안에 있는 병설 유치원을 다녔는데, 유치원 때부터 키가 꽤 큰 편이었습니다. 매일 아침 일찍 일어나 신문을 가져와 TV 일정표를 확인하며 하루의 TV 시청 계획을 세우곤 했습니다. 이모께서는 저를 종종 TV 박사라고 부르셨습니다. 가장 좋아하던 프로그램은 '인기가요'나 '뮤직뱅크'와 같은 음악방송이었습니다.
            """)
            st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2011, 8살, 초등학교 1학년")
        st.write("""
         동생이 찾아왔습니다. "도원이는 동생이 있는 게 좋겠어?"라는 클리셰 같은 질문에 그렇다고 대답한 탓일까요. 동생과 나이 차는 7살, 도원이가 기저귀 갈아줘야 하는 거 아니냐는 친척들의 농담 속에서도 기뻤습니다. 어머니는 동생이 왔을 즈음 나이가 꽤 있으셔서 병원에 주로 머무르셨습니다. 집에는 어머니의 어머니, 서울 할머니가 오셔서 저를 돌봐주셨습니다. 막연히 두렵다가도 기대되는 시간이었습니다.
         동생은 아주 작았고 성질이 사나웠습니다. 말을 못 해서인지 소리를 자주 질렀고 자주 울었습니다. 실제로 기저귀를 갈아보기도 했습니다. 동생이 제 손 위에 오줌만 싸지 않았더라면 더 자주 돌보지 않았을까요. 걸어 다니기 시작한 동생은 틈만 나면 소파에 누워 있는 저의 배 위로 뛰어내렸고 머리카락을 잡아당겼습니다.
         그즈음 저의 생활은 동생과 판타지 소설 사이를 오가는 일뿐이었습니다. 위인전만 주야장천 읽더니 이제는 판타지 소설이었습니다. 저는 해리포터, 나니아 연대기 등의 고전적인 소설을 몇 번이고 반복해 읽었습니다. 실제로 해리포터는 매년 한 번씩 읽어서 6번 넘게 읽은 상태로 초등학교를 졸업했습니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2014년, 11살, 초등학교 4학년")
        st.write("""
         집에서 걸어서 40분, 언덕 위에 있는 노원정보도서관은 제가 아주 좋아하는 장소였습니다. 자기 전에 책을 소리 내 몇 번이고 읽어준 보람이 있는지 저는 책을 아주 좋아했기 때문입니다. 주변에서 똑똑하다며 칭찬해 주는 게 좋아서 어머니가 읽는 책을 읽기도 했습니다. 비록, 열 장도 채 못 읽고 내려놓았지만요. 도서관에서도 지적 허영을 채우기 위해 어린이 열람실을 벗어나 청소년 열람실에 가기 시작했습니다. 제가 처음 일본 소설을 읽은 것도 이때입니다. 서가를 오가다 어쩌다 집어 든 얇은 책은 남매 근친을 다른 일본 문학이었습니다. 이 때문인지 저는 20살이 넘을 때까지 일본 소설을 찾아 읽지는 않는 편입니다. 그 흔한 히가시노 게이고의 소설마저도 한 편도 안 읽었으니 말입니다.
         청소년 열람실에서 나쁜 일만 있었던 건 아닙니다. 아주 긴 시간 동안 사랑하게 된 소설도 만났습니다. 전민희 작가의 룬의 아이들이란 소설입니다. 흔히 고상하게 여기는 셰익스피어, 박완서 등의 글이 아니라 창피하게 생각한 적도 있습니다. 초등학교 4학년 여름방학 때 읽은 이후로 매년 여름방학 때마다 다시 읽었습니다. 책이 1부와 2부를 합쳐 15권이기 때문에 학기 중에 읽기에는 너무 길었기 때문입니다.
         글쓰기도 시작했습니다. 어릴 적 음악방송 프로그램을 보고 춤을 췄던 것처럼 좋아하면 하고 싶어지는 성향이기 때문입니다. 실제로 여름방학 숙제로 단편 소설을 써 가기도 했습니다. 또 부모님께는 비밀이었지만, 네이버 웹소설 아마추어 게시판에 소설을 연재해 보기도 했습니다. 매일 조회수와 '좋아요' 수, 관심 수를 캡처해서 폴더에 모아두었습니다. 초등학생이 쓴 유치찬란한 소설을 읽던 사람들은 누구였을까요? 그들도 초등학생이었을까요.
         """)
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2017, 14살, 중학교 1학년")
        st.write("""
         중학교의 위상은 높았습니다. 공부가 본격적으로 어려워지는 건 중학교 때부터라는 말이 돌았습니다. 다행히도 저는 자유학년제의 혜택을 받을 수 있었습니다. 학교가 끝나면 늘 놀이터로 가서 저녁 8시까지 친구들과 수다를 떨고 술래잡기를 하고 떡볶이를 먹었습니다. 사춘기가 온 친구들 사이에 껴서 눈치를 보기도 했습니다.
         안 좋은 일도 있었습니다. 같은 반 남학생들이 단체 카카오톡 방에서 제 친구들을 성희롱했기 때문입니다. 메시지 기록에는 저에 대한 욕도 있었습니다. 저는 잘 웃지 않는다는 이유로 남성 혐오자가 아니냐며 언급되어 있었습니다. 대부분의 사람은 즐겁거나 재미있을 때만 웃을 텐데 말입니다. 선생님은 얼굴이 어떻고 가슴이 어떻고 하는 성희롱에 화가 난 제 친구들의 말을 듣고 공감해 주셨습니다. 그러나 친구들이 원하는 대로 학교 폭력 위원회를 열지는 않으셨습니다. 저와 단둘이 면담했을 때 학교 폭력 위원회가 열리면 일이 귀찮아진다고 말씀하셨습니다. 그 이후로 부모님의 근무지가 바뀌어서 이사를 하게 되었습니다. 사춘기가 찾아왔고 저를 이루고 있는 사회도 한 차례 커졌습니다. 왜 선생님은 원칙대로 하지 않으셨을까요? 그리고 왜 저희는 학교폭력 전담 경찰관과 학교폭력예방법에 대해 잘 몰랐을까요. 저는 저의 세상에 대해 생각하는 일이 더 많아졌습니다.
         """)
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2019, 16살, 중학교 3학년")
        st.write("""
         고등학교 진학을 앞두고 진로를 결정할 때가 됐습니다. 경기도 남양주시는 아주 촌 동네는 아닙니다. 도시라고 할 수 있을 정도입니다. 그래도 농어촌 전형의 혜택을 받을 수 있을 정도로 휑한 동네이기도 합니다. 저는 생활기록부를 중심으로 심사하여 합격생을 뽑는 수시전형으로 대학입시를 치를 생각이었습니다. 고등학교 3년 동안 일관성 있는 생활기록부가 중요한 전형입니다.
         소설을 아주 좋아했고 소설 쓰기도 좋아했습니다. 소설 쓰기는 저의 주된 취미였습니다. 소설을 일주일 넘게 쓰지 않으면 제 안에서 글자가 쌓이는 기분을 느낄 정도로 말입니다. 하지만 글을 써서 성공할 자신도 없었고 지금 좋다는 이유로 정했다가 안 좋아지면 어떡할까요.
         저는 제가 좋아하는 일 대신 저의 성향과 가치관에 맞는 일에 대해 생각해 보았습니다. 안정적이고 공익을 직접적으로 실현하는 직업이요. 그게 바로 사서였습니다. 정보와 인터넷 포털사이트 자체에 대한 관심도 있었습니다. 도서관의 이 많은 도서는 어떻게 관리되고 분류될까요? 검색어와 연관된 웹사이트는 어떻게 알아내는 걸까요? 저는 진로를 문헌정보학과로 결정한 다음 집에서 도보 5분 거리의 고등학교에 진학했습니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2022년, 19살, 고등학교 3학년")
        st.write("""
         도서부와 학생회 활동으로 바쁜 고등학교 생활이 끝났습니다. 저는 9월 대학에 제출할 자기소개서까지 모두 제출한 다음 수능 최저 기준을 맞히기 위해 매일 6시 30분에 일어나 수능시험의 모의고사를 풀었습니다. 3개월 정도 매일 수능을 한 번씩 치르고 오답하며 지냈습니다. 공부에만 매진해도 되는 기간이었습니다. 수능을 계획했던 것보다 조금 더 잘 보고 예상했던 대로 대학교에 입학 서류를 등록했습니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.header("성인 시절")
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2023, 20살, 대학교 1학년, 중앙대학교 문헌정보학과 입학")
        st.write("""
         문헌정보학 공부는 예상했던 대로 저와 잘 맞았습니다. 흥미로웠고 즐거웠습니다. 어려운 부분도 있었지만, 고등학교 때보다 훨씬 폭 넓고 깊은 공부는 저를 즐겁게 했습니다. 처음으로 집을 벗어나 기숙사에 살게 되었습니다. 기숙사에 붙어 있는 헬스장도 써 보고, 오트밀도 먹어보고, 질릴 때까지 학식도 먹어봤습니다. 룸메이트는 항상 좋았고 시설도 좋았습니다. 즐거운 1년이었습니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2024, 21살, 대학교 2학년, 첫 예술 관련 강의 ACT 수강")
        st.write("""
         저는 글쓰기에서 도망친 걸까요? 자신이 꿈꿨던 대로 만화창작과에 입학한 중학교 친구의 이야기를 듣다 보니 그런 의문이 들었습니다. 글쓰기를 취미 삼아 몇 번 쓴 적 있지만, 꾸준히 쓰지는 못했습니다. 저의 본업은 문헌정보학 공부였고 친구의 본업은 만화 창작이었습니다. 이전과 달리 줄어든 글쓰기 실력을 보고 나니 의욕도 꺾였습니다.
         그러다 ACT 강의를 들었고 한 명의 친구와 같이 하나의 문서를 펼쳐놓고 동시에 시나리오를 썼습니다. 그렇게 좋은 글도 아니었고 같이 쓰다 보니 마음에 안 드는 부분도 있었습니다. 그래도 아주 오랜만에 글쓰기가 저의 2순위가 아니라 1순위에 들어온 순간이었습니다. 당장 하지 않아도 괜찮습니다. 꾸준히 좋아하다 보면 좋아하는 일을 하게 된다고 생각했습니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2028, 26살, 대학교 4학년")
        st.write("""
         1년간 휴학을 하느라 조금 늦어지긴 했지만, 드디어 졸업입니다. 2년 전부터 꾸준히 준비해 왔던 만큼 사서직 공무원 시험에 단번에 붙었습니다. 법원 사서직에 합격했다는 사실에 기뻤고 마침내 자신의 힘으로 돈을 번다는 점도 좋았습니다. 적응은 힘들었지만, 좋았습니다. 우리 사회를 구성하고 있는 가장 기본적인 기반은 법입니다. 법만큼 명시적으로 우리 사회를 규정하는 문헌은 없습니다. 그런 법이 실제로 사용되는 현장에서 정보를 조직하고 관리한다는 건 제가 고대해 왔던 일이었습니다. 역시 사서직이라 해야 할까요. 직장 동료 및 선배분들이 다 친절하셨기 때문입니다. 이전에 대학교에 다니면서 국립중앙도서관에서 주말 계약직 직원으로 2년간 근무했을 때부터 사서 분들은 다 친절하다는 걸 알고 있었습니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2032, 30살")
        st.write("""
         업무를 할 때 여유가 생겼습니다. 공무원의 좋은 점은 국민과 공익을 위해 일한다는 점입니다. 저는 회사의 이익을 최우선으로 두고 근무하지 않아도 됩니다. 하루의 3분지 1, 남은 인생의 3분지 1에 해당하는 시간 동안 저는 공익을 위해 시간을 쓸 수 있습니다. 일을 하다 보니 궁금하고 부족한 부분도 자세히 알게 됐습니다. 저는 입사 할 때부터 모아둔 적금을 깨 중앙대학교 문헌정보학과 대학원에 들어갔습니다. 국립중앙도서관 사서, 공립 고등학교 사서 교사 등등 다양한 사람들이 이미 대학원 수업을 듣고 있었습니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2037, 35살")
        st.write("""
         업무를 할 때 여유가 생겼습니다. 공무원의 좋은 점은 국민과 공익을 위해 일한다는 점입니다. 저는 회사의 이익을 최우선으로 두고 근무하지 않아도 됩니다. 하루의 3분지 1, 남은 인생의 3분지 1에 해당하는 시간 동안 저는 공익을 위해 시간을 쓸 수 있습니다. 일을 하다 보니 궁금하고 부족한 부분도 자세히 알게 됐습니다. 저는 입사 할 때부터 모아둔 적금을 깨 중앙대학교 문헌정보학과 대학원에 들어갔습니다. 국립중앙도서관 사서, 공립 고등학교 사서 교사 등등 다양한 사람들이 이미 대학원 수업을 듣고 있었습니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2044, 42살")
        st.write("""
         동생이 결혼했습니다. 30 중반에서야 하는 결혼이지만, 늦은 나이는 아닙니다. 동생은 늘 그렇듯 시끄러웠고 신나 보였습니다. 저도 신났습니다. 제가 소파에 누워 있으면 제 발을 핥아서 소파에서 쫓아내곤 했던 동생이 언제 이렇게 큰 걸까요? 웨딩드레스를 입은 동생은 아주 꼿꼿하게 서 있었고 웨딩 마치 아래를 천천히 걸어왔습니다. 휘청이거나 넘어질 뻔한 적도 없었습니다. 저는 맛집과 디저트 카페를 찾아다닐 정도로 음식을 좋아하지만, 그날 결혼식 뷔페의 맛은 잘 기억하지 못합니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
        st.subheader("2062, 60살")
        st.write("""
         100세 시대를 넘어 150세 시대가 오고 있습니다. 아이가 태어나지 않아 이렇게나 일꾼이 부족한 데도 정년퇴직은 60살에 하라니. 좋기도 하고 좋지 않기도 합니다. 그래도 그간 허리띠도 조르고 투자해 둔 돈도 있어서 공무원 연금과 함께하면 남은 인생은 평화롭습니다. 저는 제 친구와 저 둘 중 한 명이 중병에 걸리지 않기를 바라며 은퇴했습니다. 주로 하는 일은 글쓰기입니다. 사서 일을 하느라 손목과 손가락이 아파서, 긴 시간 동안 자판을 두드리지는 못합니다. 그래서 운동도 꾸준히 하고 영양제도 잘 챙겨 먹습니다. 주말마다 동네 공공도서관에 가서 동화책 읽어주기 봉사를 합니다. 이제 아이들은 까치 같습니다. 분명히 있는데 길에서 찾아보려고 하면 잘 보이지 않습니다. 그런 까치 같은 아이들을 모아 놓고 어릴 적 어머니께서 저에게 읽어주셨던 것처럼 동화책을 읽어줍니다.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "과제 소개":
    st.markdown(f"""
    <style>
    .main-title {{
        text-align: center;
        font-size: 3rem;
        color: #FF4500;
    }}
    .sub-title {{
        text-align: center;
        font-size: 1.5rem;
        color: #333333;
    }}
    .sidebar .sidebar-content {{
        background-color: #FFEDD5;
    }}
    </style>
    <h1 class="main-title">Human Library</h1>
    <p class="sub-title">2054년 기록</p>
    """, unsafe_allow_html=True)

    def main3():
        st.markdown("</div>", unsafe_allow_html=True)
        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
            st.subheader("Human Library란?")
            st.write("""
             휴먼 라이브러리는 다양한 경험과 지식을 가진 사람을 책처럼 등록하여, 등록된 휴먼북(사람책)을 대출·열람하는 서비스를 제공하는 도서관입니다. 사람이 한 명, 한 명이 도서관의 도서가 되는 겁니다. 최근 구직자들 사이로 실무자와의 '커피챗'을 꼭 한 번은 해 보라는 조언이 돕니다. 그만큼 한 사람의 경험과 지식이 귀하고 중하다는 뜻입니다.
            """)
            st.markdown("</div>", unsafe_allow_html=True)

        with st.container():
            st.markdown(
                """
                <div style="border: 1px solid #FF4500; padding: 2px; border-radius: 15px; background-color: #FF4500;">
                """, 
                unsafe_allow_html=True
            )
            st.subheader("나의 인생 연출하기")
            st.write("""
            여태까지도 그랬고, 앞으로도 저의 인생은 도서관과 떨어지지 않을 것 같습니다. 그런 점에서 저의 인생 자체가 도서관이 되는 Human Library를 떠 올렸습니다. 제가 아주 나이를 먹고 도서관에서 Human Book이 되었다는 전제로 이번 과제를 작성하였습니다. 이 챗봇은 제가 입력한 내용을 토대로 ChatGPT가 저에 대한 답변을 작성합니다.
             제가 60살쯤이 되면, 개인과 개인이 대면 약속을 잡는 Human Book보다는 AI를 활용한 Human Book이 더 많고 자주 이용될 거 같다고 생각하여 이번 과제를 수행하였습니다. 챗봇 부분을 제외하고 AI를 사용한 부분은 일절 없습니다! 만약, AI를 활용한 챗봇 형태가 부적절하다면 '약력' 페이지에 작성해 둔 글을 참고하여 과제 채점해 주시기를 바랍니다.
             챗봇에는 '약력' 페이지의 글과 저의 MBTI에 관한 내용, 일기의 일부 내용을 교육했습니다!
             참고로 질문을 너무 많이 하지는 말아주세요. 질문을 할 때마다 ChatGPT 사용 요금이 나갑니다. 이번 학기 관련 내용으로 과제를 하고 충전한 돈이 조금 남아있긴 합니다.
             한 학기 동안 고생 많으셨습니다. 저도 즐거웠습니다.
            """)
            st.markdown("</div>", unsafe_allow_html=True)
         
        



if __name__ == "__main__":
    if page == "😃AI챗봇":
        main1()
    elif page == "📄약력":
        main2()
    elif page == "과제 소개":
        main3()
