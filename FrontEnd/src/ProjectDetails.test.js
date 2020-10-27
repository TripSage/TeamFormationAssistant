import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import ProjectDetails from "./ProjectDetails";

it('Trail Test', () => {
  expect(true).toBeTruthy();
});

it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(
<BrowserRouter>
  <ProjectDetails />
</BrowserRouter>,
div
  );
  ReactDOM.unmountComponentAtNode(div);
})

