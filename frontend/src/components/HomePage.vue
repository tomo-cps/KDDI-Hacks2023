<template>
  <v-app id="inspire">  
    <v-main>

      <v-container>
        <v-row>
          <v-col>
            <h1>2023年度  KDDIハッカソン学会  &nbsp; 会場:クサヤ温泉</h1>
          </v-col>
        </v-row>
        <v-row>
          <v-col
            v-for="card in cards"
            :key="card.title"
            cols="4"
          >

            <v-card class="mr-3" max-width="320" @click="navigateToChat(card.page)">
              <div
              :style="{
              width: '100%',
              paddingTop: '66.66%',
              backgroundImage: `url(${card.image})`,
              backgroundPosition: 'center',
              backgroundRepeat: 'no-repeat',
              backgroundSize: 'cover'
              }"
              ></div>
              <v-card-subtitle>{{card.subtitle}}</v-card-subtitle>
              <v-card-title class="text-wrap" style="line-height: 1.2; height: 6.0em; overflow: hidden;font-size: 1.2em;">{{card.title}}</v-card-title>
              
            </v-card>
            
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { useRouter } from 'vue-router';
export default {
  name: 'HomePage',
  setup() {
  const router = useRouter();

  const navigateToChat = (page) => {
    router.push({ name: page });
  };

  return { navigateToChat };
  },


  data() {
  return {
    cards: [
      //IT (1ページ目)
      { title: '深層学習による画像認識を用いたコンクリート建造物の変状検出に関する研究', subtitle: '青島亘佐', image: '/images/it.png' , page: 'chat1' },
      //建築 (2ページ目)
      { title: '「戦後『新建築』誌に見られた建築家の創作の主題」に対する討論', subtitle: '奥山信一', image: '/images/construction.png' , page: 'chat2' },
      //材料 (3ページ目)
      { title: '超塑性ナイロン系アロイの構造と物性', subtitle: '熱海智也', image: '/images/material.png' , page: 'chat3' },
      //深層学習 (4ページ目)
      { title: '深層畳み込みニューラルネットワークに基づくコンクリート表面のひび割れ検出システム', subtitle: '野村泰稔', image: '/images/deeplearning.png' , page: 'chat4' },
      //経済 (5ページ目)
      { title: 'Twitterにおける共通の関心を持つユーザのレコメンド', subtitle: '貴志 将考', image: '/images/hoge.png' , page: 'chat5' },
      //音楽 (6ページ目)
      { title: '音楽と感情に関する研究の展開', subtitle: '森数馬', image: '/images/music.png' , page: 'chat6' },
    ]
  }
}
  
}


</script>