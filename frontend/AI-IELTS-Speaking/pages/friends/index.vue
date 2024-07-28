<script setup lang="ts">
import { ref } from 'vue';
import { showToast } from 'vant';

const chosenContactId = ref('1');
const list = ref([
    {
    id: '1',
    name: '张三',
    tel: '13000000000',
    isDefault: true,
    },
    {
    id: '2',
    name: '李四',
    tel: '1310000000',
    },
]);

const onAdd = () => showToast('新增');
const onEdit = (contact) => showToast('编辑' + contact.id);
const onSelect = (contact) => showToast('选择' + contact.id);


</script>

<template>
    <div class="friends-container">
        <van-contact-list
            v-model="chosenContactId"
            :list="list"
            default-tag-text="默认"
            @add="onAdd"
            @edit="onEdit"
            @select="onSelect"
        />
    </div>
</template>

<style lang="scss">
.friends-container {
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>
