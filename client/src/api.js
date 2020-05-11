/* eslint-disable import/prefer-default-export */
import axios from 'axios';

const baseUrl = 'http://localhost:5000';

const baseHandler = res => res.data;

export const fetchTextList = async () => axios.get(`${baseUrl}/textlist`).then(baseHandler);

export const fetchText = async textId => axios.get(`${baseUrl}/textlist/${textId}`).then(baseHandler);

export const addText = async text => axios.post(`${baseUrl}/textlist`, text).then(baseHandler);

export const fetchSentences = async textId => axios.get(`${baseUrl}/sentences/${textId}`).then(baseHandler);

export const fetchRelatedSentences = async (textId, sentenceId) => axios.get(`${baseUrl}/sentences/${textId}/related/${sentenceId}`).then(baseHandler);
