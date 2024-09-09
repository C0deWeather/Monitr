import "./login.css"

function Login(){
    console.log("working")
    return(
        <div>
            <form id="loginForm">
                <input type="email" placeholder="email" required/>
                <input type="password" placeholder="password" required/>
                <button type="submit" class="btn">login</button>
                <a href="">Forgot password</a>
            </form>
        </div>
    )
}
export default Login