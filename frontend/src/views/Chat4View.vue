<template>
  <v-row justify="center">
    <v-col cols="5" class = "my-6">
    <h2>2023年度  KDDIハッカソン学会  &nbsp; 会場:クサヤ温泉</h2>
    <v-card class="pa-2 my-6">
      <v-img
        src= "/images/deeplearning.png"
        contain
        :style="{width: '100%', height: 'auto'}"
      ></v-img>
    <v-card-title class="headline mb-0" style="white-space: pre-line;">
      深層畳み込みニューラルネットワークに基づくコンクリート表面のひび割れ検出システム
    </v-card-title>
    <v-card-subtitle class="subtitle-1">
      野村泰稔
    </v-card-subtitle>
    <v-card-text>
      キーワード：
      <br>
      深層畳み込みニューラルネットワーク (Deep convolutional neural network)
      <br>
      表面検査 (Surface inspection)
      <br>
      ひび割れ検出 (Crack detection)
      <br>
      イメージ処理 (Image processing)
      <br>
      機械学習 (Machine learning)
      <br>
      パターン認識 (Pattern recognition)
    </v-card-text>
  </v-card>
    </v-col>
    <v-col cols="5">
      <ChatPage1 />
    </v-col>
  </v-row>
</template>

<script>
import { defineComponent } from 'vue';

// Components
import ChatPage1 from '@/components/ChatPage1.vue';

export default defineComponent({
  name: 'Chat1View',

  components: {
    ChatPage1,
  },
});
</script>