
import React from 'react';
import { useEffect } from 'react';
import { useState } from 'react';
import {Format} from '../components/Format/format';
import {Location} from '../components/Location/location';
import {Weather} from '../components/Weather/weather';

export const api = ()=> {

    const [api, setApi]= useState( [] )

    useEffect(()=> {
        fetch('/api').then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => console.log(data))
    }, [])

    return(
        <>
        <Format/>
        <Location/>
        <Weather/>

        </>
    )
}

