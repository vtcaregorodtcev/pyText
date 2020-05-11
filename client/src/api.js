/* eslint-disable import/prefer-default-export */
import axios from 'axios';

const baseUrl = 'http://localhost:5000';

const baseHandler = res => res.data;

export const fetchTextList = async () => axios.get(`${baseUrl}/textlist`).then(baseHandler);

export const addText = async text => axios.post(`${baseUrl}/textlist`, text);
