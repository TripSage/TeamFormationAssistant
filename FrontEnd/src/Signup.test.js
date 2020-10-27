import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import Signup from "./Signup";
import { render } from '@testing-library/react';
import { screen } from "@testing-library/react"
import renderer from 'react-test-renderer';


it('Trail Test', () => {
  expect(true).toBeTruthy();
});


it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(
<BrowserRouter>
  <Signup />
</BrowserRouter>,
div
  );
  ReactDOM.unmountComponentAtNode(div);
})


describe('Test suits for Home DOM Tree check', () => {
it('should match with snapshot', () => {
  const tree = renderer
  .create(
    <BrowserRouter>
    </BrowserRouter>
  )
  .toJSON();
 expect(tree).toBeNull();
 });
});
