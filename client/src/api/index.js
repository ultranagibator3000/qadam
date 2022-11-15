import axios from "axios"
import { useRouter } from "vue-router"
import { useAuthStore } from "../stores/auth"

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
    timeout: 30 * 1000,
    headers: {
        "Content-Type": "application/json"
    }
})

api.interceptors.request.use(
    (config) => {
        const authStore = useAuthStore()

        const { authTokens, authenticated, tokenExpired, updateToken } = authStore

        if (authenticated() && tokenExpired()) {
            updateToken()
        }

        config.headers.Authorization = `Bearer ${authTokens.accessToken}`

        return config
    },
    (error) => {
        console.log(`API call error: ${error}`)
        return Promise.reject(error)
    }
)

api.interceptors.response.use(
    (response) => {
        return response
    },
    (error) => {
        if (error.response.status == 401) {
            const router = useRouter()
            router.push({ name: "login" })
        }

        console.log(`API call error: ${error}`)
        return Promise.reject(error)
    }
)

export const login = async (credentials) => {
    await api.post(credentials)
        .then((response) => {
            return response
        })
        .catch((error) => {
            console.log(`API call error: ${error}`)
            return Promise.reject(error)
        })
}

export default api
