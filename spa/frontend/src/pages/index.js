import React from "react";
import AppLayout from "components/AppLayout";
import { Route } from "react-router-dom";
import About from "./About";
import Home from "./Home";
import AccountsRoutes from "./accounts";

function Root(){
    return(
        <AppLayout>
            최상위 컴포넌트
            <Route exact path="/" component={Home}/>    
            <Route exact path="/about" component={About}/>
            <Route path="/accounts" component={AccountsRoutes}/>
        </AppLayout>
    )
}

export default Root;