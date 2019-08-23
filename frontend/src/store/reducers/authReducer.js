const initialState = {
  email: null,
  token: null,
  authLoading: false,
  authError: null
};



const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case "AUTH_START":
      return {
        ...state,
        authLoading: true,
        authError: null
      }
    case "AUTH_SUCCESS":
      return {
        ...state,
        token: action.token,
        email: action.email,
        authLoading: false,
        authError: null
      }
    case "AUTH_ERROR":
      return {
        ...state,
        authLoading: false,
        authError: action.error,
      }
    case "AUTH_LOGOUT":
      return {
        ...state,
        email: null,
        token: null,
        authLoading: false,
        authError: null
      }
    default:
      return state
  }
}


export default authReducer;