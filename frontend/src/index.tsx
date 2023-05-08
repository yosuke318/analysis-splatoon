import React from "react";
import {createRoot} from 'react-dom/client';


import {RecoilRoot} from "recoil";

const rootElement = document.getElementById("root");

const root = createRoot(rootElement as Element);

root.render(
    <RecoilRoot>

    </RecoilRoot>
);
