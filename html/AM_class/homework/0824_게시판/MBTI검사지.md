<style>
    *{padding: 0; margin: 0; /* list-style-type: none;    */}
#board_mask{width: 100%; height: 100vh;}

#board_wrap{margin: 0 auto; width: 1200px; height: auto; padding: 20px;}

.bd_title{
    width: 100%;
    height: auto;
    font-size: 20pt;
    font-weight: 700;
    text-align: center;
}
.bd_exp{
    width: 100%;
    height: auto;
    margin-top: 50px;
}

.bd_exp ol li{
    width: 100%;
    height: 50px;
    margin-top: 5px;
    /* padding: 2px; */
    /* list-style-type: decimal; */
    list-style-position:inside;
}
.bd_index{width: 100%; height: auto; border-collapse: collapse;}
.board_title{font-size: 15pt; font-weight: 700;}
.board_title div{text-align: center; border: 1px solid black;}

.bli div{
    padding: 5px;
    display : table-cell;
    border-bottom: 1px solid black;
    border-left: 1px solid black;
    border-right: 1px solid black;
}

.bli{display: flex; height: auto;line-height: auto;}
.num{width: 10%; text-align: center;}
.case{width: 40%; text-align: left;}
.check{width: 10%; text-align: center;}
.index2{width: 100%; height: auto; margin-bottom: 20px;}
.sum1{width: 530px;}
.check2_1{width: 103px;}
.sum2{width: 415px;}
.check2_2{width: 104px;}
.result{width: 100%;}
.check2_3{text-align: center;}
.check2_3 input{width: 50px;}

</style>

<div id="board_mask">
        <div id="board_wrap">
            <div class="bd_title">MBTI 성격유형 간이 검사지</div>
            <div class="bd_exp">※실시요령
                <ol>
                    <li>다음 각 번호별로 제시되어 있는 두 개의 문장을 읽고 나에게 보다 많이 해당되는 것에 ○ 합니다.</li>
                    <li>○ 개수를 세어 합계란에 쓰고 점수가 큰 쪽의 유형을 □ 안에 씁니다.</li>
                    <li>□ 안에 쓴 영어 알파벳을 맨 나중에 차례대로 4가지를 붙여 씁니다.</li>
                </ol>
            </div>
            <div class="bd_index">
                <ul class="board_list">
                    <li class="board_title bli">
                        <div class="num">번호</div>
                        <div class="case">E 유형</div>
                        <div class="check">표시</div>
                        <div class="case">I 유형</div>
                        <div class="check">표시</div>
                    </li>
                </ul>
                <ul class="board_list">
                    <li class="board_count bli">
                        <div class="num">1</div>
                        <div class="case">나는 여러 친구들과 많이 사귀는 편이다.</div>
                        <div class="check"><input type="checkbox" name="q1"></div>
                        <div class="case">나는 몇 명의 친구들과 깊이 사귀는 편이다.</div>
                        <div class="check"><input type="checkbox" name="q1"></div>
                    </li>
                </ul>
                <ul class="board_list">
                    <li class="board_count bli">
                        <div class="num">2</div>
                        <div class="case">계발활동을 갈 때 새로운 친구들을 만나는 것이 신난다.</div>
                        <div class="check"><input type="checkbox"></div>
                        <div class="case">새로운 계발활동 부서에 갈 때 처음 보는 친 구들과 앞으로 어떻게 지낼까 걱정이다.</div>
                        <div class="check"><input type="checkbox"></div>
                    </li>
                </ul>
                <ul class="board_list">
                    <li class="board_count bli">
                        <div class="num">3</div>
                        <div class="case">처음 보는 친구들을 만나면 내가 먼저 말한다.</div>
                        <div class="check"><input type="checkbox"></div>
                        <div class="case">처음 보는 친구들을 만나면 다른 친구가 나에게 먼저 말한다.</div>
                        <div class="check"><input type="checkbox"></div>
                    </li>
                </ul>
                <ul class="board_list">
                    <li class="board_count bli">
                        <div class="num">4</div>
                        <div class="case">나의 생각이나 느낌을 다른 사람에게 이야기하는 편이다.</div>
                        <div class="check"><input type="checkbox"></div>
                        <div class="case">나의 생각이나 느낌을 내 마음 속에 간직하는 편이다.</div>
                        <div class="check"><input type="checkbox"></div>
                    </li>
                </ul>
                <ul class="board_list">
                    <li class="board_count bli">
                        <div class="num">5</div>
                        <div class="case">나는 친구들과 함께 하는 놀이가 좋다.</div>
                        <div class="check"><input type="checkbox"></div>
                        <div class="case">나는 나 혼자 재미있게 하는 놀이가 좋다.</div>
                        <div class="check"><input type="checkbox"></div>
                    </li>
                </ul>
                <ul class="board_list">
                    <li class="board_count bli">
                        <div class="num">6</div>
                        <div class="case">나는 많은 친구들에게 이야기하길 좋아한다.</div>
                        <div class="check"><input type="checkbox"></div>
                        <div class="case">나는 친한 친구들에게 이야기하기를 좋아한다.</div>
                        <div class="check"><input type="checkbox"></div>
                    </li>
                </ul>
                <ul class="board_list">
                    <li class="board_count bli">
                        <div class="num">7</div>
                        <div class="case">친구들과 함께 공부하면 잘된다.</div>
                        <div class="check"><input type="checkbox"></div>
                        <div class="case">나 혼자 공부하면 더 잘 된다.</div>
                        <div class="check"><input type="checkbox"></div>
                    </li>
                </ul>
                <ul class="board_list">
                    <li class="board_count bli">
                        <div class="num">8</div>
                        <div class="case">나는 나의 생각과 느낌을 말로 표현하는 것이 편하다. </div>
                        <div class="check"><input type="checkbox"></div>
                        <div class="case">나는 나의 생각과 느낌을 글로 표현하는 것이 편하다.</div>
                        <div class="check"><input type="checkbox"></div>
                    </li>
                </ul>
                <ul class="board_list">
                    <li class="board_count bli">
                        <div class="num">9</div>
                        <div class="case">주위 사람들은 내가 활발하다고 말한다.</div>
                        <div class="check"><input type="checkbox"></div>
                        <div class="case">주위 사람들은 내가 얌전하다고 말한다.</div>
                        <div class="check"><input type="checkbox"></div>
                    </li>
                </ul>
            </div>
            <div class="index2">
            <ul class="board_list2">
                <li class="board_count bli">
                    <div class="sum1">합계</div>
                    <div class="check2_1 check2_3"><input type="number" min="0" max="9"></div>
                    <div class="sum2">합계</div>
                    <div class="check2_2 check2_3"><input type="number" min="0" max="9"></div>
                </li>
            </ul>
            <ul class="board_list2">
                <li class="board_count bli">
                    <div class="result">나의 에너지 방향은 ? </div>
                </li>
            </ul>
        </div>
        <div class="bd_index">
            <ul class="board_list">
                <li class="board_title bli">
                    <div class="num">번호</div>
                    <div class="case">S 유형</div>
                    <div class="check">표시</div>
                    <div class="case">N 유형</div>
                    <div class="check">표시</div>
                </li>
            </ul>
            <ul class="board_list">
                <li class="board_count bli">
                    <div class="num">1</div>
                    <div class="case">나는 친구들에게 내가 직접 보고 들은 것에 대 해 얘기하는 것을 좋아한다. </div>
                    <div class="check"><input type="checkbox" name="q1"></div>
                    <div class="case">난 친구들에게 내가 상상한 것을 이야기하는 것을 좋아한다.</div>
                    <div class="check"><input type="checkbox" name="q1"></div>
                </li>
            </ul>
            <ul class="board_list">
                <li class="board_count bli">
                    <div class="num">2</div>
                    <div class="case">나는 실제로 있었던 사람이나 사실에 대한 책을 좋아한다.</div>
                    <div class="check"><input type="checkbox"></div>
                    <div class="case">나는 상상으로 지어낸 이야기를 좋아한다.</div>
                    <div class="check"><input type="checkbox"></div>
                </li>
            </ul>
            <ul class="board_list">
                <li class="board_count bli">
                    <div class="num">3</div>
                    <div class="case">어려운 일에 부딪히면 하던 일을 잘못 한다.</div>
                    <div class="check"><input type="checkbox"></div>
                    <div class="case">어려운 일에 부딪히면 도전하고 싶은 마음이 생긴다.</div>
                    <div class="check"><input type="checkbox"></div>
                </li>
            </ul>
            <ul class="board_list">
                <li class="board_count bli">
                    <div class="num">4</div>
                    <div class="case">나는 무엇을 할 때 전에 배웠던 대로 하는 것이 편하다.</div>
                    <div class="check"><input type="checkbox"></div>
                    <div class="case">나는 무엇을 할 때 새로운 방법을 생각해서 해 볼 때 더 재미있다.</div>
                    <div class="check"><input type="checkbox"></div>
                </li>
            </ul>
            <ul class="board_list">
                <li class="board_count bli">
                    <div class="num">5</div>
                    <div class="case">나는 그려진 그림에 색칠하기를 좋아한다.</div>
                    <div class="check"><input type="checkbox"></div>
                    <div class="case">나는 이야기 지어내기를 좋아한다.</div>
                    <div class="check"><input type="checkbox"></div>
                </li>
            </ul>
            <ul class="board_list">
                <li class="board_count bli">
                    <div class="num">6</div>
                    <div class="case">나는 현재에 최선을 다하는 것이 중요하다고 생 각한다.</div>
                    <div class="check"><input type="checkbox"></div>
                    <div class="case">나는 미래에 대한 꿈을 갖는 것이 중요하다고 생각한다.</div>
                    <div class="check"><input type="checkbox"></div>
                </li>
            </ul>
            <ul class="board_list">
                <li class="board_count bli">
                    <div class="num">7</div>
                    <div class="case">나는 선생님이 가르쳐 주신 방법대로 하는 편이다.</div>
                    <div class="check"><input type="checkbox"></div>
                    <div class="case">나는 나 스스로 나만의 방법을 만들어서 하는 편이다.</div>
                    <div class="check"><input type="checkbox"></div>
                </li>
            </ul>
            <ul class="board_list">
                <li class="board_count bli">
                    <div class="num">8</div>
                    <div class="case">내가 좋아하는 책은 읽은 것이라도 또 읽는다.  </div>
                    <div class="check"><input type="checkbox"></div>
                    <div class="case">나는 새로운 다른 책을 읽는 것이 좋다.</div>
                    <div class="check"><input type="checkbox"></div>
                </li>
            </ul>
            <ul class="board_list">
                <li class="board_count bli">
                    <div class="num">9</div>
                    <div class="case">나는 부지런하고 성실하다는 얘기를 듣는 편이다</div>
                    <div class="check"><input type="checkbox"></div>
                    <div class="case">나는 기발하고 엉뚱하다는 얘기를 듣는 편이다</div>
                    <div class="check"><input type="checkbox"></div>
                </li>
            </ul>
        </div>
        <div class="index2">
        <ul class="board_list2">
            <li class="board_count bli">
                <div class="sum1">합계</div>
                <div class="check2_1 check2_3"><input type="number" min="0" max="9"></div>
                <div class="sum2">합계</div>
                <div class="check2_2 check2_3"><input type="number" min="0" max="9"></div>
            </li>
        </ul>
        <ul class="board_list2">
            <li class="board_count bli">
                <div class="result">나의 인식 기능은? </div>
            </li>
        </ul>
    </div>
        </div>
    </div>