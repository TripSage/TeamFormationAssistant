import React from "react";
import ReactDOM from "react-dom";
import MemoryRouter, { BrowserRouter } from "react-router-dom";
import App from "./App";
import {render, cleanup} from "@testing-library/react";
import Home from "./Home";

it('Trail Test', () => {
  expect(true).toBeTruthy();
});

it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(
<BrowserRouter>
  <App />
</BrowserRouter>,
div
  );
  ReactDOM.unmountComponentAtNode(div);
})
//
// it('invalid path should redirect to 404', () => {
//   const wrapper = mount(
//     <MemoryRouter initialEntries={[ '/random' ]}>
//       <App/>
//     </MemoryRouter>
//   );
//   expect(wrapper.find(Home)).toHaveLength(0);
//   expect(wrapper.find(NotFoundPage)).toHaveLength(1);
// });



