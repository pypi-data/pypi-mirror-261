#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import sys

from ipcheck.app.common_config import CommonConfig
from ipcheck.app.valid_test_config import ValidTestConfig
from ipcheck.app.rtt_test_config import RttTestConfig
from ipcheck.app.speed_test_config import SpeedTestConfig

SECTION_COMMON = 'common'
SECTION_COMMON_PREFIX = ''

SECTION_VALID = 'valid test'
SECTION_VALID_PREFIX = 'vt_'

SECTION_RTT = 'rtt test'
SECTION_RTT_PREFIX = 'rt_'

SECTION_DOWNLOAD = 'speed test'
SECTION_DOWNLOAD_PREFIX = 'st_'


class Config(CommonConfig):

    def __init__(self, config_path):
        # common 部分配置
        # 测试ip 源, 可选ip、ip cidr、文本(读取ip、ip cidr)、zip 压缩包(遍历其中的txt 文本，读取ip、ip cidr)
        self.ip_source = ''
        self.ip_port = 443
        self.out_file = 'best_ips.txt'
        # 仅仅在运行时支持修改，不支持文件配置
        self.verbose = False
        self.white_list = None
        self.block_list = None

        # 可用性valid test测试选项
        # 是否测试可用性
        self.vt_enabled = True
        # 限制参与valid 测试的ip 数量
        self.vt_ip_limit_count = 1500
        # 可用性检测域名
        self.vt_host_name = 'cloudflare.com'
        # 可用性检测路径, 固定的，取决于cloudflare
        self.vt_path = '/cdn-cgi/trace'
        # 可用性测试多线程数量
        self.vt_thread_num = 64
        # 可用性测试时的网络请求重试次数
        self.vt_max_retry = 2
        # 可用性测试的网络请求timeout, 单位 s
        self.vt_timeout = 3
        # 可用性测试检测的key
        self.vt_check_key = 'h'
        # 是否检测地区信息
        self.vt_get_loc = True

        # 延时rtt test 测试选项
        self.rt_enabled = True
        # 限制参与rtt 测试的ip 数量
        self.rt_ip_limit_count = 1000
        # rtt tcpping 间隔
        self.rt_interval = 0.2
        # rtt 测试多线程数量
        self.rt_thread_num = 16
        # rtt 测试的网络请求timeout, 单位 s
        self.rt_timeout = 3
        # rtt 测试网络请求重试次数
        self.rt_max_retry = 2
        # rtt 测试及格线
        self.rt_max_rtt = 300
        # 最大丢包率
        self.rt_max_loss = 100
        # rtt 测试次数
        self.rt_test_count = 10

        # 下载速度测试 speed test 测试选项
        # 是否测试下载速度
        self.st_enabled = True
        # 参与测速ip 的数量限制
        self.st_ip_limit_count = 1000
        # 测试下载文件的域名
        self.st_host_name = 'cloudflaremirrors.com'
        # 测试下载文件的路径
        self.st_file_path = '/archlinux/iso/latest/archlinux-x86_64.iso'
        # 下载测试时网络请求的重试次数
        self.st_max_retry = 2
        # 下载测试网络请求timeout, 单位 s
        self.st_timeout = 3
        # 下载时长限制, 单位 s
        self.st_download_time = 10
        # 最小达标速度, 单位 kB/s
        self.st_download_speed = 5000
        # 是否执行快速测速开关
        self.st_fast_check = False

        self.__update(config_path)

    def __update(self, path):
        variables = vars(self)
        parser = configparser.ConfigParser()
        parser.read(path, 'utf-8')
        for section in parser.sections():
            prefix = ''
            if section == SECTION_COMMON:
                prefix = SECTION_COMMON_PREFIX
            elif section == SECTION_VALID:
                prefix = SECTION_VALID_PREFIX
            elif section == SECTION_RTT:
                prefix = SECTION_RTT_PREFIX
            elif section == SECTION_DOWNLOAD:
                prefix = SECTION_DOWNLOAD_PREFIX
            else:
                # 不要parse 无关的section
                break
            for option in parser.options(section):
                value = parser.get(section, option)
                key = '{}{}'.format(prefix, option)
                if not self.check_key_valid(key):
                    continue
                original_value = variables.get(key)
                type_expr = None
                if original_value:
                    type_of_original_value = type(original_value)
                    if type_of_original_value == str:
                        type_expr = 'str'
                if type_expr:
                    expr = "self.{} = '{}'".format(key, value)
                else:
                    expr = 'self.{} = {}'.format(key, value)
                # print(expr)
                exec(expr)


    def check_key_valid(self, key):
        variables = vars(self)
        for k, _ in variables.items():
            if k == key:
                return True
        return False


    def get_valid_test_config(self) -> ValidTestConfig:
        return ValidTestConfig(self)

    def get_rtt_test_config(self) -> RttTestConfig:
        return RttTestConfig(self)

    def get_speed_test_config(self) -> SpeedTestConfig:
        return SpeedTestConfig(self)


if __name__ == '__main__':
    test_config = Config(sys.argv[1])
    print(test_config)


