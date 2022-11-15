import { ref, watch } from "vue"
import { defineStore } from "pinia"
import api, { login as _login } from "../api"
import jwt_decode from "jwt-decode"

export const useAuthStore = defineStore(() => {
    const authTokens = ref({
        accessToken: "",
        refreshToken: ""
    })

    if (localStorage.getItem("authTokens")) {
        authTokens.value = JSON.parse(localStorage.getItem("authTokens"))
    }

    watch(
        authTokens,
        (newValue) => {
            localStorage.setItem("authTokens", JSON.stringify(newValue))
        },
        { deep: true }
    )

    const authenticated = () => {
        return authTokens.value.accessToken.length > 0 &&
            authTokens.value.refreshToken.length > 0
    }

    const tokenExpired = () => {
        if (authTokens.value.accessToken.length > 0) {
            return null
        }

        const { exp } = jwt_decode(authTokens.value.accessToken)

        if (Date.now() >= exp * 1000) {
            return true
        } else {
            return false
        }
    }

    const setAccessToken = (newValue) => {
        authTokens.value.accessToken = newValue
    }

    const setRefreshToken = (newValue) => {
        authTokens.value.refreshToken = newValue
    }

    const updateToken = async () => {
        await api.post({
            refresh: authTokens.value.refreshToken
        })
            .then((response) => {
                setAccessToken(response.data.access)
            })
            .catch((error) => {
                console.log(error)
                return Promise.reject(error)
            })
    }

    const login = async (credentials) => {
        const data = await _login(credentials)
        
        setAccessToken(data.access)
        setRefreshToken(data.refresh)
    }

    return {
        authTokens,
        authenticated, 
        tokenExpired,
        setAccessToken, 
        setRefreshToken,
        updateToken,
        login
    }
})
