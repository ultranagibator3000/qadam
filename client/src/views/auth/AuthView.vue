<template>
    <div class="container flex">
        <form @submit.prevent="submitForm">
            <div class="form-control">
                <input v-model="credentials.username" type="email" placeholder="Эл. адрес" required />
            </div>

            <div class="form-control">
                <input v-model="credentials.password" type="password" placeholder="Пароль" required />
            </div>

            <input class="btn btn-primary" type="submit" value="Войти">
        </form>
    </div>
</template>

<script setup>
import { ref } from "vue"
import { useAuthStore } from "../../stores/auth"

const authStore = useAuthStore()

const credentials = ref({
    email: "",
    password: ""
})

const submitForm = async () => {
    await authStore.login(credentials.value)
}

</script>
