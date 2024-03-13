<table width=100%>
  <tr>
    <td colspan=2><strong>
    aws-ec2-tool
      </strong>&nbsp;&nbsp;&nbsp;&nbsp;
    </td>
  </tr>
  <tr>
    <td width=15%><img src=https://raw.githubusercontent.com/Robot-Wranglers/aws-ec2-tool/master/img/icon.png style="width:150px"></td>
    <td>
        A small toolbox for working with EC2.  Including:<br/><br/>
          <strong>hop:</strong> a CLI for SSHing to EC2 using SSM-backed keys
    <br/><br/>
    <a href=https://pypi.python.org/pypi/aws-ec2-tool/><img src="https://img.shields.io/pypi/l/aws-ec2-tool.svg"></a>
    <a href=https://pypi.python.org/pypi/aws-ec2-tool/><img src="https://badge.fury.io/py/aws-ec2-tool.svg"></a>
    <a href="https://github.com/Robot-Wranglers/aws-ec2-tool/actions/workflows/python-test.yml"><img src="https://github.com/Robot-Wranglers/aws-ec2-tool/actions/workflows/python-test.yml/badge.svg"></a>
    </td>
  </tr>
</table>

---------------------------------------------------------------------------------

<div class="toc">
<ul>
<li><a href="#overview">Overview</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#using-hop-with-iac">Using hop with IaC</a></li>
</ul>
</div>


---------------------------------------------------------------------------------

## Overview

(Placeholder)

See [setup.cfg](setup.cfg) to find the latest info about required versions of boto.

See the [Usage section](#usage) for more details

---------------------------------------------------------------------------------

## Installation

See [pypi](https://pypi.org/project/aws-ec2-tool/) for available releases.

```bash
pip install aws-ec2-tool
```

---------------------------------------------------------------------------------

## Usage

After installation, you can invoke this tool as either `hop` or `python -m hop`.

Usage info follows:

```bash
$ hop --help

Usage: hop [OPTIONS] COMMAND [ARGS]...

  ...placeholder..
```

---------------------------------------------------------------------------------

## Using hop with IaC

It's most convenient and powerful if you're using `hop` under circumstances that guarantee that your SSH keys are already stored in SSM according to strong conventions.  In other words.. it's a good idea to manage this stuff with infrastructure-as-code.

Here's some quick information and examples about how to get started doing that with [terraform](http://terraform.io).  Here's some of the resources involved:

* [aws_key_pair resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/key_pair)
* [aws_instance resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance)

Let's get keys stored in SSM first.  The commands below use the `ssm` command via the [aws-ssm-tool](https://github.com/Robot-Wranglers/aws-ssm-tool).  (This tool is an explicit dependency of this project; it's already installed if you ran `pip` for this project.)

```bash
# generate a new keypair
$ ssh-keygen -b 2048 -t rsa -f test.key -q -N ""
$ ls test.key*
test.key  test.key.pub

# put keypairs into SSM at a predictable location.
$ ssm put /your_org/keypairs/test/pub --file test.key.pub
$ ssm put /your_org/keypairs/test/pem --file test.key

# optional: get the value you set, if you want to test
$ ssm get /your_org/keypairs/test/pub
```
The keypair is in SSM now, but there's no actual keypair that we can use with EC2 yet.  Create the keypair from what's stored in SSM with terraform like this:

```terraform
data "aws_ssm_parameter" "pub_key" {
  name = "/org_name/keypairs/key_name/pub"
}

resource "aws_key_pair" "appservers" {
  key_name   = "appservers-key"
  public_key = data.aws_ssm_parameter.pub_key.value
}
```

Now you can use this keypair with EC2.

```terraform

data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "appserver-test" {
  ami           = data.aws_ami.ubuntu
  instance_type = "t3.micro"
  key_name = aws_key_pair.appservers.key_name
  tags = {
    Name = "my-appserver-name"
  }
  subnet_id = ".."
  vpc_security_group_ids=[".."]
}
```
