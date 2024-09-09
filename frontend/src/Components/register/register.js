import "./register.css";

function Register() {
  return (
    <div>
      <form id="regForm">
        <input type="text" placeholder="Username" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="password" />
        <button type="submit" class="btn">Register</button>
      </form>
    </div>
  );
}
export default Register;
