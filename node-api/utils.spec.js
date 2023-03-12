const utils = require('./utils');
// const assert = require('assert');
const should = require('should');

describe('utils.js 모듈의 capitalize() 함수는 ', () => {
    it('문자열의 첫번째 문자를 대문자로 변환한다', () => {
        const result = utils.capitialize('hello');
        // assert.equal(result, 'Hello');
        result.should.be.equal('Hello');
    })
})
