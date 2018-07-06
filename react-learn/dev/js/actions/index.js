export const selectUser = (user) => {
  console.log(user.first +  ' clicked');
  return {
      type: "USER_SELECTED",
      payload: user 
    }
};