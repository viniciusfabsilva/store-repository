import React from "react";
import { useForm } from "react-hook-form";
import axios from "axios";
import "./UserCreateForm.css";

function UserCreateForm() {
  const { register, handleSubmit, errors } = useForm();

  const onSubmit = values => {
    axios
      .post("http://localhost:8000/users/", values)
      .then(response => console.log(response))
      .catch(error => console.error(error));
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="user-create-form">
      <div className="user-register">
      <label className="">
          <div className="label">
            Nome:
            <input type="text" {...register("first_name", { required: true })} className="input"/>
          </div>
        </label>
        <label className="">
          <div className="label">
            Email:
            <input type="email" {...register("email", { required: true })} className="input"/>
          </div>
        </label>
        <label className="">
          <div className="label">
            Password:
            <input type="password" {...register("password", { required: true })} className="input"/>
          </div>
        </label>
        <label className="">
          <div className="label">
            Data de nascimento:
            <input type="date" {...register("birth_date", { required: true })} className="input"/>
          </div>
        </label>
      
        <input type="submit" value="Enviar" className="submit"/>
      </div>
    </form>
  );
}

export default UserCreateForm;