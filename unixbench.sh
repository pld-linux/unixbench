#!/bin/sh
WORKDIR=`mktemp -d ${TMPDIR:-/tmp}/unixbenchXXXXXX`
export UB_BINDIR=/usr/lib/unixbench
export UB_TMPDIR=$WORKDIR
export UB_RESULTDIR=$WORKDIR
export UB_TESTDIR=$WORKDIR
cp $UB_BINDIR/sort.src $UB_TESTDIR
$UB_BINDIR/Run $@
